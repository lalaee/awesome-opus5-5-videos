#!/usr/bin/env python3
"""Build inspiration.md for the /brag skill from data/videos.json.

The picks and notes live in curation.json, the intro in template.md, and the
measurements (length, cuts, sound) in measured.json, written by measure.py.
Every quote is checked against the creator's real prompt, so the output never
puts words in anyone's mouth, and every pick needs a "seen" note written after
watching it.

    python3 tools/brag-inspiration/build.py            # write inspiration.md
    python3 tools/brag-inspiration/build.py --check    # fail if it is stale
    python3 tools/brag-inspiration/build.py -o PATH    # write somewhere else
"""

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REPO_URL = "https://github.com/lalaee/awesome-opus5-5-videos"
TONES = ["default", "polished", "yc-parody", "chaotic", "deadpan", "cinematic", "app-store"]
SHOWREEL = "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out"


def norm(text):
    return " ".join(text.split())


def build():
    videos = {v["slug"]: v for v in json.loads((ROOT / "data/videos.json").read_text())}
    curation = json.loads((HERE / "curation.json").read_text())
    template = (HERE / "template.md").read_text()
    measured_path = HERE / "measured.json"
    measured = json.loads(measured_path.read_text()) if measured_path.exists() else {}
    errors = []

    def video(slug):
        if slug not in videos:
            errors.append(f"unknown slug: {slug}")
            return None
        return videos[slug]

    def link(slug):
        v = video(slug)
        return f"[@{v['author']}]({v['skillry_url']})" if v else f"@{slug}"

    if list(curation["tones"]) != TONES:
        errors.append(f"curation.json tones must be exactly {TONES}")

    sections = []
    for tone in TONES:
        picks = [e for e in curation["examples"] if e["tone"] == tone]
        if not picks:
            errors.append(f"no examples for tone {tone}")
        lines = [f"## `{tone}`", "", curation["tones"].get(tone, ""), ""]
        for e in picks:
            v = video(e["slug"])
            if not v:
                continue
            if v["prompt_partial"]:
                errors.append(f"{e['slug']}: prompt is partial")
            if norm(e["quote"]) not in norm(v["prompt"]):
                errors.append(f"{e['slug']}: quote not found in prompt: {e['quote']!r}")
            quote = f"“{e['quote']}”"
            if e.get("translation"):
                quote += f" (“{e['translation']}”)"
            if not e.get("seen"):
                errors.append(f"{e['slug']}: no 'seen' note; watch the video first (measure.py --sheets)")
            m = measured.get(e["slug"])
            if not m:
                errors.append(f"{e['slug']}: not measured; run measure.py")
                continue
            facts = [f"{m['seconds']:.0f} s", "no hard cuts" if m["cuts_per_10s"] == 0 else f"{m['cuts_per_10s']:g} cuts/10 s"]
            if m["sound"] != "yes":
                facts.append("no sound")
            if m["height"] > m["width"]:
                facts.append("vertical")
            elif m["height"] == m["width"]:
                facts.append("square")
            lines.append(f"- **{link(e['slug'])}** ({' · '.join(facts)}): {quote}  ")
            lines.append(f"  **Seen:** {e['seen']}  ")
            lines.append(f"  **Borrow:** {e['borrow']}")
        sections.append("\n".join(lines) + "\n")

    unknown = {e["tone"] for e in curation["examples"]} - set(TONES)
    if unknown:
        errors.append(f"unknown tones: {sorted(unknown)}")

    cited = list(dict.fromkeys([e["slug"] for e in curation["examples"]] + re.findall(r"\{\{U:([\w-]+)\}\}", template)))
    for slug in cited:
        if slug not in measured:
            errors.append(f"{slug}: cited but not measured; run measure.py")
    stats = [measured[s] for s in cited if s in measured]
    showreels = sum(norm(v["prompt"]).lower().rstrip(".") == SHOWREEL for v in videos.values())
    out = (
        template.replace("{{TONES}}", "\n".join(sections))
        .replace("{{TOTAL}}", str(len(videos)))
        .replace("{{SHOWREEL_COUNT}}", str(showreels))
        .replace("{{REPO_URL}}", REPO_URL)
        .replace("{{N}}", str(len(stats)))
        .replace("{{N_WINDOW}}", str(sum(15 <= m["seconds"] <= 25.5 for m in stats)))
        .replace("{{N_NO_CUTS}}", str(sum(m["cuts_per_10s"] == 0 for m in stats)))
        .replace("{{N_NO_SOUND}}", str(sum(m["sound"] != "yes" for m in stats)))
    )
    out = re.sub(r"\{\{U:([\w-]+)\}\}", lambda m: (video(m.group(1)) or {}).get("skillry_url", ""), out)
    if "{{" in out:
        errors.append("unfilled placeholder in template.md")
    return out, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-o", "--output", type=Path, default=HERE / "inspiration.md")
    parser.add_argument("--check", action="store_true", help="exit 1 if the output file is out of date")
    args = parser.parse_args()

    out, errors = build()
    if errors:
        sys.exit("\n".join(errors))
    if args.check:
        if not args.output.exists() or args.output.read_text() != out:
            sys.exit(f"{args.output} is stale; rerun build.py")
        print(f"{args.output} is up to date.")
        return
    args.output.write_text(out)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
