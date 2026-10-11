import argparse
import hashlib
import json
import re
import shutil
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'config.json'
PREVIEW = ('Olá! Esta é uma amostra de narração em português brasileiro. '
           'Naquela manhã, a luz entrou pela janela e iluminou as páginas do livro. '
           'Cada capítulo guardava uma nova descoberta. Respire com calma e acompanhe esta história.')


def clean_md(text):
    text = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', text, flags=re.S)
    text = re.sub(r'```.*?```|~~~.*?~~~', '', text, flags=re.S)
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    text = re.sub(r'^\s*(?:#{1,6}\s+|>\s*|[-*+]\s+|\d+[.)]\s+)', '', text, flags=re.M)
    text = re.sub(r'^\s*([-*_])(?:\s*\1){2,}\s*$', '', text, flags=re.M)
    text = re.sub(r'[`*_]', '', text)
    return '\n\n'.join(re.sub(r'\s+', ' ', p).strip()
                       for p in re.split(r'\n\s*\n', text) if p.strip())


def chunks(text, limit):
    result, current = [], ''
    for paragraph in text.split('\n\n'):
        current = ''
        for sentence in re.split(r'(?<=[.!?…])\s+(?=[—“"A-ZÀ-Ý])', paragraph):
            if current and len(current) + len(sentence) + 1 > limit:
                result.append(current)
                current = ''
            # Limite flexivel: preserve frases inteiras, sem cortar palavras.
            current = (current + ' ' + sentence).strip()
        if current:
            result.append(current + '\n\n')
    grouped, block = [], ''
    for part in result:
        if block and len(block) + len(part) > limit:
            grouped.append(block)
            block = ''
        block += part
    if block:
        grouped.append(block)
    return grouped


def main():
    parser = argparse.ArgumentParser(description='MOSS-TTS: testes de voz e capitulos Markdown')
    parser.add_argument('--preview', action='store_true')
    parser.add_argument('--files', nargs='+', type=Path)
    parser.add_argument('--list', type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--set-voice', type=Path)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--max-chunks', type=int, help='Teste apenas os primeiros N trechos')
    parser.add_argument('--optimize', action='store_true', help='Cache da referencia e codec fora da GPU durante geracao')
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding='utf-8'))
    args.optimize = args.optimize or config.get('optimize', False)
    if args.set_voice:
        voice = args.set_voice.resolve(strict=True)
        if voice.suffix.lower() not in {'.wav', '.mp3', '.flac', '.m4a', '.ogg'}:
            parser.error('Referencia deve ser um arquivo de audio.')
        config['reference_audio'] = str(voice)
        config['voice_status'] = 'referencia_definida_aguardando_teste'
        CONFIG.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')
        print('Voz salva:', voice)
        return
    if not args.output:
        parser.error('Informe --output PASTA.')
    files = args.files or []
    if args.list:
        for line in args.list.read_text(encoding='utf-8-sig').splitlines():
            line = line.strip().strip('"')
            if line:
                path = Path(line)
                files.append(path if path.is_absolute() else args.list.resolve().parent / path)
    jobs = []
    if args.preview:
        if config.get('require_reference') and not config.get('reference_audio'):
            parser.error('Teste automatico desativado: defina uma referencia feminina brasileira com --set-voice AUDIO.')
        for i, seed in enumerate([42, 123, 2026], 1):
            jobs.append((f'voz_{i:02d}', [PREVIEW], seed, config.get('reference_audio')))
    else:
        reference = config.get('reference_audio')
        if not reference:
            parser.error('Escolha a voz com --set-voice antes de narrar capitulos.')
        Path(reference).resolve(strict=True)
        for i, path in enumerate(files, 1):
            if path.suffix.lower() != '.md':
                parser.error(f'Arquivo nao Markdown: {path}')
            text = clean_md(path.read_text(encoding='utf-8-sig'))
            if not text:
                parser.error(f'Capitulo vazio: {path}')
            name = re.sub(r'[^\w.-]+', '_', path.stem)
            parts = chunks(text, config['chunk_chars'])
            if args.max_chunks:
                if args.max_chunks < 1:
                    parser.error('--max-chunks deve ser positivo.')
                parts = parts[:args.max_chunks]
                name += '_amostra'
            jobs.append((f'{i:03d}_{name}', parts, config['seed'], reference))
    if not jobs:
        parser.error('Informe --preview, --files ou --list.')
    if args.dry_run:
        for name, parts, seed, reference in jobs:
            print(name, len(parts), 'trechos;', sum(map(len, parts)), 'caracteres')
        return
    import numpy as np
    import soundfile as sf
    import torch
    import torchaudio
    # O processor remoto usa torchaudio.load, que depende das DLLs TorchCodec.
    def load_audio_soundfile(uri, frame_offset=0, num_frames=-1, normalize=True, channels_first=True, **kwargs):
        data, sample_rate = sf.read(str(uri), start=frame_offset,
            frames=num_frames, dtype='float32', always_2d=True)
        tensor = torch.from_numpy(data.T.copy() if channels_first else data.copy())
        return tensor, sample_rate
    torchaudio.load = load_audio_soundfile
    from huggingface_hub import snapshot_download
    from transformers import AutoModel, AutoProcessor
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA indisponivel. Verifique o ambiente .venv e o driver.')
    torch.backends.cuda.enable_cudnn_sdp(False)
    local = snapshot_download(config['model'])
    processor = AutoProcessor.from_pretrained(local, trust_remote_code=True)
    processor.audio_tokenizer = processor.audio_tokenizer.to('cuda')
    if args.optimize:
        encode_original = processor.encode_audios_from_path
        reference_cache = {}
        def encode_cached(paths, n_vq=None):
            paths_list = [paths] if isinstance(paths, str) else list(paths)
            key = (tuple(str(p) for p in paths_list), n_vq)
            if key not in reference_cache:
                processor.audio_tokenizer.to('cuda')
                with torch.inference_mode():
                    reference_cache[key] = [x.clone() for x in encode_original(paths_list, n_vq)]
            return [x.clone() for x in reference_cache[key]]
        processor.encode_audios_from_path = encode_cached
    model = AutoModel.from_pretrained(local, trust_remote_code=True,
        attn_implementation='sdpa', torch_dtype=torch.bfloat16).to('cuda').eval()
    rate = processor.model_config.sampling_rate
    args.output.mkdir(parents=True, exist_ok=True)
    for name, texts, seed, reference in jobs:
        synthesis_config = {k: v for k, v in config.items() if k not in {'output_format', 'mp3_bitrate'}}
        identity = dict(model=config['model'], snapshot=local, texts=texts, seed=seed, settings=synthesis_config, pipeline_version=2,
                        reference=reference, reference_hash=hashlib.sha256(Path(reference).read_bytes()).hexdigest() if reference else None)
        digest = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()[:16]
        part_dir = args.output / 'trechos' / f'{name}_{digest}'
        part_dir.mkdir(parents=True, exist_ok=True)
        paths = []
        for index, text in enumerate(texts, 1):
            path = part_dir / f'{index:04d}.wav'
            paths.append(path)
            if path.exists():
                info = sf.info(path)
                if info.frames > 0 and info.samplerate == rate:
                    print('Reutilizando', name, index, flush=True)
                    continue
            print(f'Gerando {name}: trecho {index}/{len(texts)}', flush=True)
            torch.manual_seed(seed + index - 1)
            kw = {'reference': [reference]} if reference else {}
            message = processor.build_user_message(text=text, **kw)
            batch = processor([[message]], mode='generation')
            if args.optimize:
                processor.audio_tokenizer.to('cpu')
                torch.cuda.empty_cache()
            torch.cuda.synchronize()
            started = time.perf_counter()
            with torch.inference_mode():
                outputs = model.generate(input_ids=batch['input_ids'].to('cuda'),
                    attention_mask=batch['attention_mask'].to('cuda'), max_new_tokens=config.get('max_new_tokens', 2048),
                    audio_temperature=config.get('audio_temperature', 1.0),
                    audio_top_p=config.get('audio_top_p', 0.95), audio_top_k=config.get('audio_top_k', 50),
                    audio_repetition_penalty=config.get('audio_repetition_penalty', 1.1))
                torch.cuda.synchronize()
                generation_seconds = time.perf_counter() - started
                if args.optimize:
                    # Liberation du KV cache avant de recharger le codec.
                    del batch
                    torch.cuda.empty_cache()
                    processor.audio_tokenizer.to('cuda')
                decoded = processor.decode(outputs)
            if not decoded or not decoded[0].audio_codes_list:
                raise RuntimeError(f'Nenhum audio: {name}, trecho {index}')
            audio = decoded[0].audio_codes_list[0].detach().float().cpu().numpy().squeeze()
            if audio.ndim != 1 or not audio.size:
                raise RuntimeError(f'Audio invalido: {name}, trecho {index}')
            if not np.isfinite(audio).all() or np.max(np.abs(audio)) < 1e-5:
                raise RuntimeError(f'Audio silencioso ou nao finito: {name}, trecho {index}')
            if len(audio) / rate >= config.get('max_new_tokens', 2048) / 12.5 * 0.98:
                raise RuntimeError(f'Possivel truncamento: {name}, trecho {index}. Reduza o texto.')
            peak = np.max(np.abs(audio))
            if peak > 0.98:
                audio = audio * (0.98 / peak)
            temporary = path.with_suffix('.tmp.wav')
            sf.write(temporary, audio, rate, subtype='PCM_16')
            temporary.replace(path)
            print(f'TIMING generation={generation_seconds:.2f}s audio={len(audio)/rate:.2f}s optimized={args.optimize}', flush=True)
            if not args.optimize:
                del batch
            del outputs, decoded
            torch.cuda.empty_cache()
        if config.get('delivery') == 'numbered_blocks':
            ffmpeg = shutil.which('ffmpeg')
            if not ffmpeg:
                raise RuntimeError('FFmpeg nao encontrado; trechos WAV preservados.')
            block_dir = args.output / 'blocos' / name
            block_dir.mkdir(parents=True, exist_ok=True)
            manifest = []
            for index, (path, text) in enumerate(zip(paths, texts), 1):
                mp3 = block_dir / f'{name}_bloco-{index:03d}.mp3'
                temp_mp3 = mp3.with_suffix('.tmp.mp3')
                subprocess.run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-y', '-i', str(path),
                    '-codec:a', 'libmp3lame', '-b:a', config.get('mp3_bitrate', '192k'), str(temp_mp3)], check=True)
                if sf.info(temp_mp3).frames <= 0:
                    raise RuntimeError(f'MP3 vazio: {temp_mp3}')
                temp_mp3.replace(mp3)
                manifest.append(dict(block=index, file=mp3.name, text=text,
                    duration_seconds=sf.info(mp3).duration,
                    sha256=hashlib.sha256(mp3.read_bytes()).hexdigest()))
            (block_dir / 'manifesto.json').write_text(json.dumps(dict(synthesis=identity, blocks=manifest),
                ensure_ascii=False, indent=2), encoding='utf-8')
            print('Blocos MP3 concluidos:', block_dir.resolve(), flush=True)
            continue
        final = args.output / f'{name}.wav'
        temporary = final.with_suffix('.tmp.wav')
        with sf.SoundFile(temporary, 'w', samplerate=rate, channels=1, subtype='PCM_16') as target:
            for index, path in enumerate(paths):
                data, actual_rate = sf.read(path, dtype='float32')
                if actual_rate != rate:
                    raise RuntimeError(f'Taxa de audio incorreta: {path}')
                if index:
                    pause = config.get('paragraph_pause_seconds', 0.65) if texts[index-1].endswith('\n\n') else config.get('sentence_pause_seconds', 0.2)
                    target.write(np.zeros(round(rate * pause), dtype=np.float32))
                target.write(data)
        temporary.replace(final)
        final.with_suffix('.json').write_text(json.dumps(identity, ensure_ascii=False, indent=2), encoding='utf-8')
        if config.get('output_format') == 'mp3':
            ffmpeg = shutil.which('ffmpeg')
            if not ffmpeg:
                raise RuntimeError('FFmpeg nao encontrado; WAV preservado para conversao posterior.')
            mp3 = final.with_suffix('.mp3')
            temp_mp3 = final.with_suffix('.tmp.mp3')
            subprocess.run([ffmpeg, '-hide_banner', '-loglevel', 'error', '-y', '-i', str(final),
                '-codec:a', 'libmp3lame', '-b:a', config.get('mp3_bitrate', '192k'), str(temp_mp3)], check=True)
            temp_mp3.replace(mp3)
            print('MP3 concluido:', mp3.resolve(), flush=True)
        print('Concluido:', final.resolve(), flush=True)


if __name__ == '__main__':
    main()
