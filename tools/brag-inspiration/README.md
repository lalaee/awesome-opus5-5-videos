# brag inspiration

Builds `inspiration.md`, a reference file for the [/brag](https://github.com/lalaee/brag) launch-video skill. It picks launch and product videos from this collection, grouped by /brag's seven tones, with a note on what to borrow from each.

- `curation.json`: the picks, one short quote from each prompt, and the note
- `template.md`: the intro, cross-tone patterns and common failures
- `build.py`: renders the file and checks that every quote appears in the creator's real prompt

```bash
python3 tools/brag-inspiration/build.py          # regenerate after a new batch or a curation change
python3 tools/brag-inspiration/build.py --check  # fail if inspiration.md is stale
```

Copy the result to `skills/brag/references/inspiration.md` in the brag repo.
