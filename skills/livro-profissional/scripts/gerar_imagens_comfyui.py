"""Gera cenas sequencialmente pela API local do ComfyUI e permite retomar o lote."""
import argparse
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def api(base, path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    request = urllib.request.Request(base + path, data=data, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(error.read().decode(errors='replace')) from error


def graph(scene, style):
    resolution = scene.get('resolucao', 768)
    return {
        '1': {'class_type': 'UnetLoaderGGUF', 'inputs': {'unet_name': 'qwen-image-2.1-UC-Q6_K.gguf'}},
        '2': {'class_type': 'CLIPLoader', 'inputs': {'clip_name': 'qwen3vl_8b_int8_convrot.safetensors', 'type': 'qwen_image', 'device': 'cpu'}},
        '3': {'class_type': 'VAELoader', 'inputs': {'vae_name': 'qwen_image_2.1_vae_bf16.safetensors'}},
        '4': {'class_type': 'TextEncodeQwenImage21', 'inputs': {'clip': ['2', 0], 'prompt': style + '\n' + scene['prompt'], 'negative_prompt': scene.get('negativo', 'blurry, low quality, watermark, text'), 'resolution': resolution}},
        '5': {'class_type': 'KSampler', 'inputs': {'model': ['1', 0], 'positive': ['4', 0], 'negative': ['4', 1], 'latent_image': ['4', 2], 'seed': scene['seed'], 'steps': scene.get('passos', 30), 'cfg': scene.get('cfg', 4.0), 'sampler_name': 'euler', 'scheduler': 'simple', 'denoise': 1.0}},
        '6': {'class_type': 'VAEDecode', 'inputs': {'samples': ['5', 0], 'vae': ['3', 0]}},
        '7': {'class_type': 'SaveImage', 'inputs': {'images': ['6', 0], 'filename_prefix': 'livros/capitulo_%03d_cena_%03d' % (scene['capitulo'], scene['cena'])}}
    }


def save_manifest(path, manifest):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('cenas', type=Path)
    parser.add_argument('--saida', type=Path, required=True)
    parser.add_argument('--url', default='http://127.0.0.1:8188')
    parser.add_argument('--timeout', type=int, default=7200)
    parser.add_argument('--validar', action='store_true', help='Confere nós e gera workflows sem enfileirar imagens')
    args = parser.parse_args()
    if urllib.parse.urlparse(args.url).hostname not in ('127.0.0.1', 'localhost', '::1'):
        parser.error('Este pipeline aceita somente um servidor local.')
    book = json.loads(args.cenas.read_text(encoding='utf-8-sig'))
    scenes = book['cenas']
    identifiers = [(s['capitulo'], s['cena']) for s in scenes]
    if len(set(identifiers)) != len(identifiers):
        parser.error('Capítulo/cena duplicados no roteiro.')
    info = api(args.url, '/object_info')
    args.saida.mkdir(parents=True, exist_ok=True)
    manifest_path = args.saida / 'manifesto-imagens.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {}
    for scene in scenes:
        if scene['capitulo'] < 1 or scene['cena'] < 1:
            parser.error('Capítulo e cena devem ser positivos.')
        scene.setdefault('seed', int(hashlib.sha256(json.dumps(scene, sort_keys=True).encode()).hexdigest()[:12], 16))
        workflow = graph(scene, book.get('estilo', ''))
        for node in workflow.values():
            if node['class_type'] not in info:
                raise RuntimeError('Nó ausente: ' + node['class_type'])
            schema = info[node['class_type']].get('input', {})
            fields = schema.get('required', {}) | schema.get('optional', {})
            for name, value in node['inputs'].items():
                definition = fields.get(name)
                if definition and isinstance(definition[0], list) and value not in definition[0]:
                    raise RuntimeError(f"Opção ou arquivo indisponível: {node['class_type']}.{name} = {value}")
        key = 'capitulo_%03d_cena_%03d' % (scene['capitulo'], scene['cena'])
        fingerprint = hashlib.sha256(json.dumps(workflow, sort_keys=True).encode()).hexdigest()
        destination = args.saida / (key + '.png')
        previous = manifest.get(key, {})
        if previous.get('workflow_sha256') == fingerprint and destination.exists() and hashlib.sha256(destination.read_bytes()).hexdigest() == previous.get('imagem_sha256'):
            print('Preservado', key, flush=True)
            continue
        if destination.exists():
            raise RuntimeError(f'{destination} já existe com outra configuração. Use outra pasta de saída para preservar a versão anterior.')
        (args.saida / (key + '-workflow-api.json')).write_text(json.dumps(workflow, indent=2, ensure_ascii=False), encoding='utf-8')
        if args.validar:
            print('Nós disponíveis:', key, flush=True)
            continue
        start = time.monotonic()
        if previous.get('estado') == 'enfileirado':
            if previous.get('workflow_sha256') != fingerprint:
                raise RuntimeError('Cena pendente com outro workflow. Confira a fila e use outra pasta: ' + key)
            prompt_id = previous['prompt_id']
            queued = api(args.url, '/queue')
            if not api(args.url, '/history/' + prompt_id) and not any(item[1] == prompt_id for item in queued['queue_running'] + queued['queue_pending']):
                raise RuntimeError('Cena pendente não encontrada no servidor. Confira os arquivos do ComfyUI antes de reenviar: ' + prompt_id)
        else:
            result = api(args.url, '/prompt', {'prompt': workflow})
            prompt_id = result['prompt_id']
            manifest[key] = {'estado': 'enfileirado', 'prompt_id': prompt_id, 'workflow_sha256': fingerprint, 'cena': scene}
            save_manifest(manifest_path, manifest)
        print('Enfileirado', key, prompt_id, flush=True)
        while time.monotonic() - start < args.timeout:
            history = api(args.url, '/history/' + prompt_id).get(prompt_id)
            if history:
                if history.get('status', {}).get('status_str') == 'error':
                    raise RuntimeError(json.dumps(history['status'], ensure_ascii=False))
                images = history.get('outputs', {}).get('7', {}).get('images', [])
                if images:
                    break
                raise RuntimeError('Execução terminou sem imagem: ' + json.dumps(history))
            time.sleep(3)
        else:
            raise TimeoutError('Prazo excedido; a tarefa pode continuar no ComfyUI. Consulte a fila antes de reenviar: ' + prompt_id)
        query = urllib.parse.urlencode(images[0])
        with urllib.request.urlopen(args.url + '/view?' + query, timeout=120) as response:
            pixels = response.read()
        if not pixels.startswith(b'\x89PNG\r\n\x1a\n'):
            raise RuntimeError('Resposta não é PNG.')
        destination.write_bytes(pixels)
        manifest[key] = {'arquivo': destination.name, 'estado': 'gerado; aguardando inspeção e aprovação', 'cena': scene, 'workflow_sha256': fingerprint, 'imagem_sha256': hashlib.sha256(pixels).hexdigest(), 'prompt_id': prompt_id, 'segundos': round(time.monotonic() - start, 1), 'modelo': 'abenzerps/Qwen-Image-2.1-Uncensored-GGUF Q6_K', 'licenca': 'Qwen Research; autorização comercial separada necessária'}
        save_manifest(manifest_path, manifest)
        print('Gerado', destination, manifest[key]['segundos'], 's', flush=True)


if __name__ == '__main__':
    main()
