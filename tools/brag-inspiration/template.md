# Inspiration: launch videos that worked

Real videos people made with Claude Opus 5.5 by having it write the animation as code (HTML, Canvas, SVG, WebGL), the same way /brag-slim works. Picked from the {{TOTAL}}-video collection at [awesome-opus5-5-videos]({{REPO_URL}}): only full prompts, mostly launch and product videos, grouped by /brag tone.

Every note was written after watching the video, not from its prompt. **Seen** is what is on screen, with timings; **Borrow** is the idea worth taking. The quote is what the creator asked for, which is often not what they got. Length, cuts and sound are measured (`measure.py`).

## How to use this file

- **When:** after you can answer the Step 1 questions, before you commit to an angle. Read the section below and the one for your tone; skim one neighbouring tone if the project sits between two.
- **Take ideas, not content.** Borrow structures, camera ideas, pacing, transitions and build techniques. Never borrow another project's copy, claims, numbers, brand or characters, and never mention these creators in the video.
- **One or two ideas per video.** The project still sets the angle. If nothing here fits, ignore it: specific beats borrowed.
- **Not their lengths.** Most of these run longer than /brag's 15-25 s. Take structures that compress.
- **The links are optional.** Each name opens the original next to a remake. Everything you need is written here, so the file works offline.

## What the {{N}} videos show

- **The hook is readable within about 1.5 s.** Most launch videos here state their hook that fast, and the ones that take 2 s or more feel it: the viewer's problem in one line ([@deedydas]({{U:deedydas-252537}}), [@kmasiff]({{U:kmasiff-549880}})), the project's own tagline ([@hqmank]({{U:hqmank-241156}})), a live counter ([@deifosv]({{U:deifosv-786581}})), or a wall of real output ([@viktoroddy]({{U:viktoroddy-402509}})). Openings that spend 1.5-2 s on black or a lone dot are films (title sequences, short stories), and they feel slow anywhere else.
- **Problem first, then the product.** The strongest launch videos open on the viewer's problem in one or two short lines ("Docs here. Chats there.", "The same reports. The same price checks.") and only then show the product.
- **One claim, one real screen per scene.** The most common skeleton: a short headline beside a real screen, one idea each ([@kmasiff]({{U:kmasiff-549880}}), [@charlesmendez]({{U:charlesmendez-476517}}), [@iammxfschr]({{U:iammxfschr-955831}})).
- **The end card says how to get it.** Logo, one line, then a URL, an install command, an App Store search or a button. Nearly every launch video ends this way.
- **Calm or fast, rarely in between.** {{N_NO_CUTS}} of the {{N}} have no hard cuts at all; they move with morphs, camera moves and crossfades. The energetic ones run 5-9 cuts per 10 s ([@reflex_cloud]({{U:reflex-cloud-304046}}), [@jhylee95]({{U:jhylee95-452427}})).
- **Most run long.** Only {{N_WINDOW}} of the {{N}} land in 15-25 s. A /brag run in the wild took 81 s ([@VisheshBaghell]({{U:visheshbaghell-119508}})), and morph sequences drifted to two or three times the length asked ([@AnnaCher___]({{U:annacher-433425}}), [@HowDevelop]({{U:howdevelop-733090}})).
- **Plan for no sound.** {{N_NO_SOUND}} of the {{N}} have no audio or a silent track, and feeds autoplay muted anyway. "The story must also work muted." ([@HowDevelop]({{U:howdevelop-733090}})): a short caption under or beside each visual does it.
- **Corner labels are the default look; skip them.** HUD brackets, corner timecodes and "frame 120/900" labels appear in 6 of these videos. One prompt banned them: "Avoid the frames and texts on the corners which are typical ai made giveaways!" ([@souravbhar871]({{U:souravbhar871-477361}})), and the result is cleaner for it. A label that belongs to the story is fine, like a late-night clock ticking in the corner ([@xelandre]({{U:xelandre-687413}})).
- **Loop it.** The last frame equals the first in [@verbove]({{U:verbove-268381}}), [@techhalla]({{U:techhalla-498547}}) and [@johnsavage_ai]({{U:johnsavage-ai-427263}}), so they play forever in a feed.
- **Build techniques that hold up:** "every frame a pure function of time so my renderer can screenshot it" ([@parkerrex]({{U:parkerrex-701462}})); "First render one frame per beat as a contact sheet. Fix anything cramped or broken" ([@verbove]({{U:verbove-268381}})); "aim for half the speed you'd default to" ([@jake11moran]({{U:jake11moran-414633}})).

## What went wrong, and the fix

- **Too fast, not professional, bad music.** One creator's follow-up after the first pass: "it is a bit too fast and bumpy", "This is not a professional-looking video", "can you choose a royalty-free song online? You are clearly not a good song maker." ([@sachaarbonel]({{U:sachaarbonel-673648}})). The version they ended with is calm: pastel background, serif lines, long holds (see `polished`).
- **No video at the end.** "where is the video? I only see a config file" (translated from German, [@iammxfschr]({{U:iammxfschr-955831}})). Always render and hand over the MP4; their final one is under `polished`.
- **A slow first two seconds.** A lone dot on black for 2 s ([@dale_vaz]({{U:dale-vaz-879074}})), a typed line before anything happens ([@maxalexweber]({{U:maxalexweber-459784}})), a title that is readable only at 2.5 s ([@mattbean]({{U:mattbean-917572}})).
- **Too long.** A 102 s showreel ([@wani_shola]({{U:wani-shola-459278}})), 42 s for a 14 s brief ([@AnnaCher___]({{U:annacher-433425}})), 81 s for a /brag run.
- **Borrowed images.** Pasted meme stills ([@supremebeme]({{U:supremebeme-306746}})) are someone else's art; draw your own gags.
- **Generic showreels.** {{SHOWREEL_COUNT}} videos in the collection come from one prompt ("make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are…"). They look alike because the prompt has no product in it. /brag's whole job is the opposite: specific to one project.

{{TONES}}
---

_Generated by `tools/brag-inspiration/build.py` in [awesome-opus5-5-videos]({{REPO_URL}}) from notes written while watching each video. Videos and prompts belong to their creators; quotes are short excerpts, linked to each original._
