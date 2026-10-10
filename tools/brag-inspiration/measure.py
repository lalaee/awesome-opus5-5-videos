#!/usr/bin/env python3
"""Watch the videos the inspiration file cites, so its notes describe what is on screen.

For every slug in curation.json and template.md this downloads the creator's original from
Skillry, measures it (length, size, hard cuts, sound) into measured.json, and with --sheets
writes a contact sheet per video (4 frames from the first 1.5 s, then 8 spread over the rest)
for a person or an agent to look at before writing a note.

    python3 tools/brag-inspiration/measure.py --cache /tmp/brag-refs --sheets /tmp/brag-sheets

Needs ffmpeg and ffprobe; --sheets also needs Pillow.
"""

import argparse
import io
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CLIP = 'https://media.skillry.dev/opus-5-5/{slug}/original.mp4'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'


def cited_slugs():
    curation = json.loads((HERE / 'curation.json').read_text())
    template = (HERE / 'template.md').read_text()
    slugs = [e['slug'] for e in curation['examples']] + re.findall(r'\{\{U:([\w-]+)\}\}', template)
    return list(dict.fromkeys(slugs))


def run(*args):
    return subprocess.run(args, capture_output=True, text=True, stdin=subprocess.DEVNULL).stdout


def measure(path):
    probe = json.loads(run('ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=codec_type,width,height',
                           '-of', 'json', str(path)))
    video = next(s for s in probe['streams'] if s['codec_type'] == 'video')
    seconds = float(probe['format']['duration'])
    scenes = run('ffmpeg', '-v', 'error', '-i', str(path), '-an', '-vf', "select='gt(scene,0.30)',metadata=print:file=-",
                 '-f', 'null', '-')
    cuts = [float(t) for t in re.findall(r'pts_time:([0-9.]+)', scenes)]
    sound = 'none'
    if any(s['codec_type'] == 'audio' for s in probe['streams']):
        loud = re.search(r'I:\s+(-?[0-9.]+) LUFS', subprocess.run(
            ['ffmpeg', '-hide_banner', '-i', str(path), '-af', 'ebur128=framelog=quiet', '-f', 'null', '-'],
            capture_output=True, text=True, stdin=subprocess.DEVNULL).stderr)
        lufs = float(loud.group(1)) if loud else -70.0
        sound = 'silent' if lufs <= -60 else 'yes'
    return {'seconds': round(seconds, 1), 'width': video['width'], 'height': video['height'],
            'cuts_per_10s': round(len(cuts) / seconds * 10, 1), 'sound': sound}


def sheet(path, seconds, out):
    from PIL import Image, ImageDraw, ImageFont
    times = [0.05, 0.5, 1.0, 1.5] + [2.0 + (seconds - 2.3) * i / 7 for i in range(8)]
    w, h = 480, 270
    grid = Image.new('RGB', (w * 4, h * 3), (20, 20, 20))
    draw = ImageDraw.Draw(grid)
    font = ImageFont.truetype(FONT, 18) if Path(FONT).exists() else ImageFont.load_default()
    for i, t in enumerate(times):
        png = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.2f}', '-i', str(path), '-frames:v', '1',
                              '-f', 'image2pipe', '-vcodec', 'png', '-'], capture_output=True, stdin=subprocess.DEVNULL).stdout
        if not png:
            continue
        im = Image.open(io.BytesIO(png)).convert('RGB')
        im.thumbnail((w, h))
        x, y = (i % 4) * w, (i // 4) * h
        grid.paste(im, (x + (w - im.width) // 2, y + (h - im.height) // 2))
        draw.rectangle([x + 3, y + 3, x + 76, y + 26], fill=(0, 0, 0))
        draw.text((x + 6, y + 4), f'{t:.1f}s', font=font, fill=(255, 220, 0))
    grid.save(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--cache', type=Path, required=True, help='where to keep the downloaded originals')
    parser.add_argument('--sheets', type=Path, help='also write one contact sheet per video here')
    args = parser.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    if args.sheets:
        args.sheets.mkdir(parents=True, exist_ok=True)

    measured = {}
    for slug in cited_slugs():
        path = args.cache / f'{slug}.mp4'
        if not path.exists():
            try:
                urllib.request.urlretrieve(CLIP.format(slug=slug), path)
            except OSError as e:
                sys.exit(f'{slug}: download failed ({e})')
        measured[slug] = measure(path)
        if args.sheets:
            sheet(path, measured[slug]['seconds'], args.sheets / f'{slug}.png')
        print(slug, measured[slug])
    (HERE / 'measured.json').write_text(json.dumps(measured, indent=1, sort_keys=True) + '\n')
    print(f'Wrote {HERE / "measured.json"} ({len(measured)} videos)')


if __name__ == '__main__':
    main()
