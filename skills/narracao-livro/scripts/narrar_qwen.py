import argparse,json,time,hashlib,subprocess
from pathlib import Path
from narrar import clean_md,chunks
import torch,numpy as np,soundfile as sf
from qwen_tts import Qwen3TTSModel

p=argparse.ArgumentParser()
p.add_argument('--files',nargs='+',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
p.add_argument('--dry-run',action='store_true')
a=p.parse_args()
c=json.loads((Path(__file__).resolve().parents[1]/'config.json').read_text(encoding='utf-8'))
jobs=[(i,f,chunks(clean_md(f.read_text(encoding='utf-8-sig')),c['chunk_chars'])) for i,f in enumerate(a.files,1)]
if a.dry_run:
    for i,f,parts in jobs: print(f,len(parts),'blocos')
    raise SystemExit(0)
model=Qwen3TTSModel.from_pretrained(c['model'],device_map='cuda:0',dtype=torch.bfloat16,attn_implementation='sdpa')
transcript=Path(c['reference_transcript']).read_text(encoding='utf-8')
prompt=model.create_voice_clone_prompt(ref_audio=c['reference_audio'],ref_text=transcript,x_vector_only_mode=False)
refhash=hashlib.sha256(Path(c['reference_audio']).read_bytes()).hexdigest()
for i,f,parts in jobs:
    folder=a.output/'blocos'/f'{i:03d}_{f.stem}'; folder.mkdir(parents=True,exist_ok=True)
    records=[]
    for j,text in enumerate(parts,1):
        identity=dict(model=c['model'],text=text,reference=refhash,transcript=transcript,seed=c['seed'])
        digest=hashlib.sha256(json.dumps(identity,sort_keys=True).encode()).hexdigest()
        stem=folder/f'capitulo-{f.stem}_bloco-{j:03d}'
        wav=stem.with_suffix('.wav'); mp3=stem.with_suffix('.mp3'); record=stem.with_suffix('.json')
        if record.exists() and mp3.exists():
            old=json.loads(record.read_text(encoding='utf-8'))
            if old.get('fingerprint')==digest and sf.info(mp3).frames>0:
                records.append(old); print('Reutilizando',mp3,flush=True); continue
        torch.manual_seed(c['seed']); torch.cuda.synchronize(); start=time.perf_counter()
        with torch.inference_mode():
            audios,rate=model.generate_voice_clone(text=text,language='Portuguese',voice_clone_prompt=prompt,max_new_tokens=2048)
        torch.cuda.synchronize(); elapsed=time.perf_counter()-start
        audio=np.asarray(audios[0])
        if not audio.size or not np.isfinite(audio).all(): raise RuntimeError('Audio invalido')
        if len(audio)/rate>=160: raise RuntimeError('Possivel truncamento: reduzir bloco')
        temp=stem.with_suffix('.tmp.wav'); sf.write(temp,audio,rate,subtype='PCM_24'); temp.replace(wav)
        temp=stem.with_suffix('.tmp.mp3')
        subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(wav),'-codec:a','libmp3lame','-b:a',c['mp3_bitrate'],str(temp)],check=True)
        temp.replace(mp3)
        info=dict(fingerprint=digest,file=mp3.name,text=text,duration_seconds=sf.info(mp3).duration,generation_seconds=elapsed)
        record.write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8'); records.append(info)
        print('Concluido',mp3,'generation_seconds',elapsed,flush=True)
    (folder/'manifesto.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
