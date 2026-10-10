# brag inspiration

Builds `inspiration.md`, a reference file for the [/brag](https://github.com/lalaee/brag) launch-video skill. It picks launch and product videos from this collection, grouped by /brag's seven tones. Every note is written after watching the video: what is on screen, and what is worth borrowing.

- `curation.json`: the picks, with one short quote from each prompt, a `seen` note (what is on screen, with timings) and a `borrow` note
- `template.md`: the intro, what the videos show across tones, and common failures
- `measure.py`: downloads each cited video, measures length, size, hard cuts and sound into `measured.json`, and writes contact sheets to look at
- `build.py`: renders the file, checks every quote against the creator's real prompt, and refuses picks that have no `seen` note or no measurement

## Adding or changing a pick

1. Add the slug to `curation.json` (or cite it in `template.md`).
2. Watch it: `python3 tools/brag-inspiration/measure.py --cache /tmp/brag-refs --sheets /tmp/brag-sheets`, then look at its contact sheet (4 frames from the first 1.5 s, 8 across the rest) or the video itself.
3. Write `seen` from what is on screen, then `borrow`. Don't write either from the prompt.
4. `python3 tools/brag-inspiration/build.py`, and `--check` in CI to catch a stale file.

Copy the result to `skills/brag/references/inspiration.md` in the brag repo.
