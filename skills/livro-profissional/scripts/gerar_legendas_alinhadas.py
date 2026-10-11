#!/usr/bin/env python3
"""Legendas a partir dos alinhamentos existentes, sem nova chamada ao ElevenLabs."""
import argparse
import hashlib
import json
import math
import re
from pathlib import Path

WEAK = set('a o as os um uma uns umas de da do das dos em na no nas nos para por com sem e ou que se ao aos à às'.split())


def wrap(words):
    text = ' '.join(words)
    if len(text) <= 42:
        return text
    options = []
    for i in range(1, len(words)):
        a, b = ' '.join(words[:i]), ' '.join(words[i:])
        if max(len(a), len(b)) <= 42:
            cost = abs(len(a) - len(b)) + (15 if words[i-1].lower() in WEAK else 0)
            cost -= 8 if a.endswith((',', ';', ':', '.', '!', '?')) else 0
            options.append((cost, a + '\n' + b))
    return min(options)[1] if options else None


def timestamp(seconds, sep):
    milliseconds = round(seconds * 1000)
    seconds, ms = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}{sep}{ms:03}'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True, help='Pasta do livro com entrega/filmora e entrega/audiobook-elevenlabs')
    parser.add_argument('--output', type=Path, help='Padrão: entrega/youtube do projeto')
    parser.add_argument('--basename', default='legendas-pt-BR', help='Nome dos arquivos sem extensão')
    args = parser.parse_args()
    if not args.basename or Path(args.basename).name != args.basename or args.basename in {'.', '..'}:
        parser.error('--basename deve ser apenas um nome de arquivo, sem diretórios')
    ROOT = args.project.resolve(strict=True)
    OUT = args.output.resolve() if args.output else ROOT / 'entrega/youtube'
    OUT.mkdir(parents=True, exist_ok=True)
    plan = json.loads((ROOT / 'entrega/filmora/plano-timeline.json').read_text(encoding='utf-8'))
    script = json.loads((ROOT / 'entrega/audiobook-elevenlabs/roteiro.json').read_text(encoding='utf-8'))
    blocks = {x['id']: x for x in script['blocks']}
    cues = []
    source_tokens = []
    for block in plan['audio']:
        metadata = json.loads((ROOT / f"entrega/audiobook-elevenlabs/blocos/{block['id']}.json").read_text(encoding='utf-8'))
        alignment = metadata['alignment']
        chars = alignment['characters']
        text = ''.join(chars)
        expected = blocks[block['id']]['text']
        assert text == expected, block['id']
        assert hashlib.sha256(text.encode()).hexdigest() == metadata['text_sha256']
        starts = alignment['character_start_times_seconds']
        ends = alignment['character_end_times_seconds']
        assert len(chars) == len(starts) == len(ends)
        words = [{'word': m.group(), 'start': starts[m.start()], 'end': ends[m.end()-1],
                  'paragraph': '\n' in text[m.end():m.end()+2]} for m in re.finditer(r'\S+', text)]
        source_tokens.extend(w['word'] for w in words)
        n = len(words)
        assert n, f"Bloco sem texto: {block['id']}"
        costs = [math.inf] * (n + 1)
        choices = [None] * n
        costs[n] = 0
        for i in range(n-1, -1, -1):
            for j in range(i+1, min(n, i+24)+1):
                chunk = words[i:j]
                joined = ' '.join(w['word'] for w in chunk)
                duration = chunk[-1]['end'] - chunk[0]['start']
                if len(joined) > 84 or duration > 7.0:
                    break
                display = wrap([w['word'] for w in chunk])
                if display is None:
                    continue
                ending = chunk[-1]['word']
                boundary = 0 if ending.endswith(('.', '!', '?', '…')) else 1.2 if ending.endswith((',', ';', ':')) else 3.5
                if chunk[-1]['paragraph']:
                    boundary = 0
                if ending.lower() in WEAK or ending == '—':
                    boundary += 8
                short = max(0, 1.25-duration) * 15
                score = costs[j] + 2 + boundary + short + abs(duration-4.0)*.25
                if score < costs[i]:
                    costs[i] = score
                    choices[i] = (j, display)
        assert math.isfinite(costs[0]), block['id']
        i = 0
        while i < n:
            j, display = choices[i]
            offset = block['start_seconds']
            start = offset + words[i]['start']
            spoken_end = offset + words[j-1]['end']
            next_start = offset + words[j]['start'] if j < n else block['end_seconds']
            end = min(max(spoken_end+.12, start+1.0), next_start-.01, block['end_seconds'])
            end = max(spoken_end, end)
            cues.append({'start': round(start,3), 'end': round(end,3), 'text': display, 'block': block['id']})
            i = j
    assert source_tokens == [word for c in cues for word in c['text'].split()]
    for i, cue in enumerate(cues):
        assert 0 <= cue['start'] < cue['end'] <= plan['duration_seconds']
        assert len(cue['text'].splitlines()) <= 2
        assert all(len(line) <= 42 for line in cue['text'].splitlines())
        if i:
            assert cues[i-1]['end'] <= cue['start'] + .001, (i, cues[i-1], cue)
    basename = args.basename
    srt = '\n\n'.join(f"{i}\n{timestamp(c['start'], ',')} --> {timestamp(c['end'], ',')}\n{c['text']}" for i,c in enumerate(cues,1)) + '\n'
    vtt = 'WEBVTT\n\n' + '\n\n'.join(f"{timestamp(c['start'], '.')} --> {timestamp(c['end'], '.')}\n{c['text']}" for c in cues) + '\n'
    (OUT / f'{basename}.srt').write_text(srt, encoding='utf-8')
    (OUT / f'{basename}.vtt').write_text(vtt, encoding='utf-8')
    (OUT / 'tempos-legendas.json').write_text(json.dumps(cues,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    report = {'cues':len(cues), 'blocks':len(plan['audio']), 'words_preserved':len(source_tokens),
              'source':'Alinhamento de caracteres ElevenLabs existente + início de cada bloco na timeline Filmora',
              'max_lines':2,'max_characters_per_line':42,'overlaps':0,
              'first_seconds':cues[0]['start'],'last_seconds':cues[-1]['end'],
              'max_cps':round(max(len(c['text'])/(c['end']-c['start']) for c in cues),2),
              'shorter_than_800ms':sum(c['end']-c['start']<.8 for c in cues),
              'independent_transcription':False,
              'sha256':{ext:hashlib.sha256((OUT/f'{basename}.{ext}').read_bytes()).hexdigest() for ext in ['srt','vtt']}}
    (OUT/'verificacao-legendas.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    print(f'Arquivos: {OUT / (basename + ".srt")} e {OUT / (basename + ".vtt")}')


if __name__ == '__main__':
    main()
