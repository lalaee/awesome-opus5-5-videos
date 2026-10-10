# Inspiration: launch videos that worked

Real videos people made with Claude Opus 5.5 by having it write the animation as code (HTML, Canvas, SVG, WebGL), the same way /brag-slim works. Picked from the 513-video collection at [awesome-opus5-5-videos](https://github.com/lalaee/awesome-opus5-5-videos): only full prompts, mostly launch and product videos, grouped by /brag tone.

Every note was written after watching the video, not from its prompt. **Seen** is what is on screen, with timings; **Borrow** is the idea worth taking. The quote is what the creator asked for, which is often not what they got. Length, cuts and sound are measured (`measure.py`).

## How to use this file

- **When:** after you can answer the Step 1 questions, before you commit to an angle. Read the section below and the one for your tone; skim one neighbouring tone if the project sits between two.
- **Take ideas, not content.** Borrow structures, camera ideas, pacing, transitions and build techniques. Never borrow another project's copy, claims, numbers, brand or characters, and never mention these creators in the video.
- **One or two ideas per video.** The project still sets the angle. If nothing here fits, ignore it: specific beats borrowed.
- **Not their lengths.** Most of these run longer than /brag's 15-25 s. Take structures that compress.
- **The links are optional.** Each name opens the original next to a remake. Everything you need is written here, so the file works offline.

## What the 39 videos show

- **The hook is readable within about 1.5 s.** Most launch videos here state their hook that fast, and the ones that take 2 s or more feel it: the viewer's problem in one line ([@deedydas](https://skillry.dev/ai-videos/opus-5-5/deedydas-252537), [@kmasiff](https://skillry.dev/ai-videos/opus-5-5/kmasiff-549880)), the project's own tagline ([@hqmank](https://skillry.dev/ai-videos/opus-5-5/hqmank-241156)), a live counter ([@deifosv](https://skillry.dev/ai-videos/opus-5-5/deifosv-786581)), or a wall of real output ([@viktoroddy](https://skillry.dev/ai-videos/opus-5-5/viktoroddy-402509)). Openings that spend 1.5-2 s on black or a lone dot are films (title sequences, short stories), and they feel slow anywhere else.
- **Problem first, then the product.** The strongest launch videos open on the viewer's problem in one or two short lines ("Docs here. Chats there.", "The same reports. The same price checks.") and only then show the product.
- **One claim, one real screen per scene.** The most common skeleton: a short headline beside a real screen, one idea each ([@kmasiff](https://skillry.dev/ai-videos/opus-5-5/kmasiff-549880), [@charlesmendez](https://skillry.dev/ai-videos/opus-5-5/charlesmendez-476517), [@iammxfschr](https://skillry.dev/ai-videos/opus-5-5/iammxfschr-955831)).
- **The end card says how to get it.** Logo, one line, then a URL, an install command, an App Store search or a button. Nearly every launch video ends this way.
- **Calm or fast, rarely in between.** 21 of the 39 have no hard cuts at all; they move with morphs, camera moves and crossfades. The energetic ones run 5-9 cuts per 10 s ([@reflex_cloud](https://skillry.dev/ai-videos/opus-5-5/reflex-cloud-304046), [@jhylee95](https://skillry.dev/ai-videos/opus-5-5/jhylee95-452427)).
- **Most run long.** Only 14 of the 39 land in 15-25 s. A /brag run in the wild took 81 s ([@VisheshBaghell](https://skillry.dev/ai-videos/opus-5-5/visheshbaghell-119508)), and morph sequences drifted to two or three times the length asked ([@AnnaCher___](https://skillry.dev/ai-videos/opus-5-5/annacher-433425), [@HowDevelop](https://skillry.dev/ai-videos/opus-5-5/howdevelop-733090)).
- **Plan for no sound.** 10 of the 39 have no audio or a silent track, and feeds autoplay muted anyway. "The story must also work muted." ([@HowDevelop](https://skillry.dev/ai-videos/opus-5-5/howdevelop-733090)): a short caption under or beside each visual does it.
- **Corner labels are the default look; skip them.** HUD brackets, corner timecodes and "frame 120/900" labels appear in 6 of these videos. One prompt banned them: "Avoid the frames and texts on the corners which are typical ai made giveaways!" ([@souravbhar871](https://skillry.dev/ai-videos/opus-5-5/souravbhar871-477361)), and the result is cleaner for it. A label that belongs to the story is fine, like a late-night clock ticking in the corner ([@xelandre](https://skillry.dev/ai-videos/opus-5-5/xelandre-687413)).
- **Loop it.** The last frame equals the first in [@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381), [@techhalla](https://skillry.dev/ai-videos/opus-5-5/techhalla-498547) and [@johnsavage_ai](https://skillry.dev/ai-videos/opus-5-5/johnsavage-ai-427263), so they play forever in a feed.
- **Build techniques that hold up:** "every frame a pure function of time so my renderer can screenshot it" ([@parkerrex](https://skillry.dev/ai-videos/opus-5-5/parkerrex-701462)); "First render one frame per beat as a contact sheet. Fix anything cramped or broken" ([@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381)); "aim for half the speed you'd default to" ([@jake11moran](https://skillry.dev/ai-videos/opus-5-5/jake11moran-414633)).

## What went wrong, and the fix

- **Too fast, not professional, bad music.** One creator's follow-up after the first pass: "it is a bit too fast and bumpy", "This is not a professional-looking video", "can you choose a royalty-free song online? You are clearly not a good song maker." ([@sachaarbonel](https://skillry.dev/ai-videos/opus-5-5/sachaarbonel-673648)). The version they ended with is calm: pastel background, serif lines, long holds (see `polished`).
- **No video at the end.** "where is the video? I only see a config file" (translated from German, [@iammxfschr](https://skillry.dev/ai-videos/opus-5-5/iammxfschr-955831)). Always render and hand over the MP4; their final one is under `polished`.
- **A slow first two seconds.** A lone dot on black for 2 s ([@dale_vaz](https://skillry.dev/ai-videos/opus-5-5/dale-vaz-879074)), a typed line before anything happens ([@maxalexweber](https://skillry.dev/ai-videos/opus-5-5/maxalexweber-459784)), a title that is readable only at 2.5 s ([@mattbean](https://skillry.dev/ai-videos/opus-5-5/mattbean-917572)).
- **Too long.** A 102 s showreel ([@wani_shola](https://skillry.dev/ai-videos/opus-5-5/wani-shola-459278)), 42 s for a 14 s brief ([@AnnaCher___](https://skillry.dev/ai-videos/opus-5-5/annacher-433425)), 81 s for a /brag run.
- **Borrowed images.** Pasted meme stills ([@supremebeme](https://skillry.dev/ai-videos/opus-5-5/supremebeme-306746)) are someone else's art; draw your own gags.
- **Generic showreels.** 41 videos in the collection come from one prompt ("make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are…"). They look alike because the prompt has no product in it. /brag's whole job is the opposite: specific to one project.

## `default`

Punchy, playful, clean. A small story or one clear flow, hook readable in the first second or so.

- **[@hqmank](https://skillry.dev/ai-videos/opus-5-5/hqmank-241156)** (23 s · 0.9 cuts/10 s): “like it's the hero video on its GitHub README”  
  **Seen:** The project's tagline stacks in huge condensed type, line by line, readable by 1.5 s; a cursor click-ring lands on "CLICKS.". Then the real command typed in a terminal, the agent driving a browser, and an end card with a copyable git clone command.  
  **Borrow:** When the project has a three-beat tagline, it is both the hook and the storyboard. End on the real install command, not a slogan.
- **[@jackfriks](https://skillry.dev/ai-videos/opus-5-5/jackfriks-338762)** (20 s · 0.5 cuts/10 s · vertical): “use the pig assets on new branch of lovelee to make a 9:16 short story animation”  
  **Seen:** A story caption is on screen from frame 0, the app's own pig and cat act it out, and a running counter escalates (x1, x7, x33) as the joke. The app appears only at 16.8 s, as an App Store end card.  
  **Borrow:** A tiny story with the product's own characters, and a counter that escalates. Tease the app at the end, not the start.
- **[@justincooperman](https://skillry.dev/ai-videos/opus-5-5/justincooperman-188876)** (30 s · no hard cuts): “users ask for branded images and see them added to content”  
  **Seen:** The problem as a question ("Need an on-brand image for your next email?") by 0.5 s. Then the real flow: ask in chat, the image is made, it lands in the email. A small caption pill at the bottom names each step. Ends on logo, one line and a button.  
  **Borrow:** Show the output landing where it gets used. One short caption pill per step.
- **[@mattbean](https://skillry.dev/ai-videos/opus-5-5/mattbean-917572)** (30 s · no hard cuts · no sound): “1. connect your agent 2. your agent fills out your listing and sets up redemption 3. go live!”  
  **Seen:** Hand-drawn style. A handwritten title types in and is only readable at about 2.5 s; then each of the three numbered steps draws a sketched screen, ending on a URL.  
  **Borrow:** A three-step flow is three scenes. But get the opening line readable by 1.5 s; this one is slow.
- **[@VisheshBaghell](https://skillry.dev/ai-videos/opus-5-5/visheshbaghell-119508)** (81 s · no hard cuts): “build me a product demo for my site using /brag skill. make sure to emphasize on all features”  
  **Seen:** A /brag run in the wild. Strong problem hook ("One job. Two documents.") by 1.5 s, then real app screens and one big stat. But it runs 81 s, far past /brag's 15-25 s.  
  **Borrow:** State the problem in two short sentences. And when asked for every feature, still cut to the 2-3 that fit 15-25 s.

## `polished`

Serious and restrained. Real UI, continuity instead of cuts, calm holds.

- **[@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381)** (20 s · no hard cuts · square): “Content enters after its container starts morphing and leaves before the next morph so text never overlaps”  
  **Seen:** One dark pill morphs through the product: logo, button, field, card, globe, pin, list, event card, search, logo again, so it loops. Real copy in every state ("Put me on the map"), warm off-white canvas with a soft vignette. The element stays small on a big canvas.  
  **Borrow:** One element that never cuts, real copy in every state, a loop. Zoom in closer than this did; the element should fill more of the frame.
- **[@AnnaCher___](https://skillry.dev/ai-videos/opus-5-5/annacher-433425)** (42 s · no hard cuts · square): “build a product promo from our own UI, not generic components”  
  **Seen:** The same one-shape morph, driven by a cursor through connect, loader, budget slider, chart, prompt bar and a toast, back to the start. Calm, no cuts. But it runs 42 s where the prompt asked for 7 bars (14 s), and the frame is mostly empty.  
  **Borrow:** A cursor driving every change makes UI feel used, not shown. Hold the length you planned; a morph sequence drifts long.
- **[@HowDevelop](https://skillry.dev/ai-videos/opus-5-5/howdevelop-733090)** (30 s · no hard cuts): “The story must also work muted.”  
  **Seen:** A question types word by word and is complete by 1.0 s ("What can one AI API become?"). One continuous dashed line threads every scene, and each visual has a 2-4 word caption under it ("One pattern. Every modality."). No hard cuts. Asked for 15 s, it runs 30.  
  **Borrow:** A short caption under every visual makes it work muted. A single line or path that links scenes replaces cuts.
- **[@iamMXFSCHR](https://skillry.dev/ai-videos/opus-5-5/iammxfschr-955831)** (33 s · 1.5 cuts/10 s): “so a la anthropic like?” (“kind of like Anthropic?”)  
  **Seen:** Warm off-white, a serif statement ("Open a URL.") by 0.5 s, then one real screen per claim: the database table, an accent-colour picker ("Make it yours."), a terminal update ("Updates in one command."). Ends "Self-hosted. $79 once. Source code included." with logo and URL.  
  **Borrow:** Quiet serif headlines next to real screens, one claim each. End on the terms that matter (price, licence) in one line.
- **[@sachaarbonel](https://skillry.dev/ai-videos/opus-5-5/sachaarbonel-673648)** (59 s · no hard cuts): “Create a professional product launch video with motion graphics.”  
  **Seen:** The version made after the creator's harsh feedback. Pastel gradient, serif lines stacking by 1.5 s ("The same reports. / The same price checks. / The same hours, gone."), then a headline beside a UI card per beat, with long holds. Ends on logo, a line and a waitlist button. It runs 59 s.  
  **Borrow:** Three stacked short lines make a calm problem hook. Slow holds read as expensive; cut scenes to fit 15-25 s rather than speeding them up.

## `yc-parody`

The startup-launch genre that yc-parody plays straight. Learn its conventions so you can deliver them with a straight face.

- **[@moritzkremb](https://skillry.dev/ai-videos/opus-5-5/moritzkremb-466494)** (46 s · 0.7 cuts/10 s): “very professionally edited, motion-graphics-styled product launch videos that you see people making on Twitter”  
  **Seen:** It picked Notion. The problem as scattered tools ("Docs here. Chats there." with Slack, Gmail and GitHub icons drifting in) by 1.5 s, then product screens, a logo wall with stats, and logo plus button. 46 s; 8 videos in the collection reuse this prompt.  
  **Borrow:** The genre's skeleton: scattered-tools problem, product as the one place, proof, logo. Deliver it straight and the parody does itself.
- **[@deedydas](https://skillry.dev/ai-videos/opus-5-5/deedydas-252537)** (26 s · 0.8 cuts/10 s): “make a modern slick and punchy video for a modern startup that works on inference”  
  **Seen:** The hook acts out the pain: a prompt types, "Thinking..." appears, and a wait timer ticks from 0.08 s to 2.57 s. Then "Most of inference is waiting." / "Not anymore.", a utilisation grid going 31% to 94%, a throughput number, ends on the name and "done.".  
  **Borrow:** Make the viewer feel the pain for two seconds with a running timer, then flip it. One number per beat.
- **[@viktoroddy](https://skillry.dev/ai-videos/opus-5-5/viktoroddy-402509)** (54 s · no hard cuts · no sound): “just hit 1 million monthly visitors after 8 months after launch”  
  **Seen:** Frame 0 is a tilted wall of real site thumbnails, so the hook is density. Then "One command. No API key.", "Today, we hit" and a huge "1,000,000", ending on "1M and counting." and the URL. 54 s, no sound.  
  **Borrow:** Open on a wall of the real product output. One milestone number as the turn, only if the project states it.
- **[@jhylee95](https://skillry.dev/ai-videos/opus-5-5/jhylee95-452427)** (24 s · 8 cuts/10 s): “hook in the first second, then distinct beats for product proof and AI”  
  **Seen:** One feature verb per beat in huge type, about 8 cuts per 10 s, each word sprouting a bit of product UI: "click." grows a tour tooltip, "embed." an iframe snippet, "as a demo." the real demo. Ends "always on." with "Agent online - 3:12 AM".  
  **Borrow:** One verb per beat, each turning into a piece of the real product. Fast, but every word is readable.

## `chaotic`

Fast and loud, but still edited. The good ones lock the message and let the frame go wild.

- **[@techhalla](https://skillry.dev/ai-videos/opus-5-5/techhalla-498547)** (20 s · no hard cuts · no sound · square): “Magenta/green may misregister (print offset) by 2–4px on impact frames only.”  
  **Seen:** "STOP SCROLLING" builds letter by letter in huge condensed type and is complete by 2.0 s, over a green waveform baseline. One locked line per beat, glitches only on impact, ends on the handle and loops. No sound in the file.  
  **Borrow:** Chaos with rules: locked lines in a fixed order, a strict palette, glitches only on impact frames.
- **[@kloss_xyz](https://skillry.dev/ai-videos/opus-5-5/kloss-xyz-941143)** (154 s · 4.6 cuts/10 s · vertical): “chaotic brain rot video with excellent motion + sound design”  
  **Seen:** Vertical. "you hit enter." types, then a giant red "I WAS BORN." by 1.0 s. The rest is a long typographic monologue; it runs 154 s.  
  **Borrow:** Only the opening: a typed line, then one enormous word slammed in within a second.
- **[@supremebeme](https://skillry.dev/ai-videos/opus-5-5/supremebeme-306746)** (46 s · 5.9 cuts/10 s · vertical): “make a brainrot video about the terminal. i can't escape it.”  
  **Seen:** "DAY 47" with a pixel character trapped in a terminal above a slot machine labelled "ONE MORE PROMPT" (reels: LGTM, MORE, WORKS), about 6 cuts per 10 s. The meme inserts are borrowed images, not drawn.  
  **Borrow:** One relatable metaphor (the slot machine) carries the whole joke. Draw your own gags; never paste meme images.
- **[@maxalexweber](https://skillry.dev/ai-videos/opus-5-5/maxalexweber-459784)** (18 s · 2.8 cuts/10 s): “Make a ODATANO edit that goes hard”  
  **Seen:** A typed "> connecting enterpri_" holds for 1.5 s before anything happens, then a glitch flash and hyperspace streaks. One name per beat with a huge index number behind it, white-out glitches between, ending on logo and URL.  
  **Borrow:** The fan-edit format: one name per beat, a big index number behind, a flash between. Start the energy at frame 0, not at 1.5 s.
- **[@robvjourney](https://skillry.dev/ai-videos/opus-5-5/robvjourney-237474)** (15 s · 5.3 cuts/10 s): “Go ALL OUT and make the most badass video you possibly can”  
  **Seen:** A terminal boot sequence ("$ nohandslabs --boot", lines of [ok], "no hands required") by 1.5 s, an acid-green flash, the site's own line "Companies that build themselves", "95% built by AI" in dot-matrix type, a diagonal ticker tape, ending on a waitlist button. 15 s.  
  **Borrow:** Turn the product's own copy into a boot sequence. Maximum energy works when every line is the site's real claim.

## `deadpan`

Calm, dry, literal. The premise is the joke; the delivery never winks.

- **[@_nikolajankovic](https://skillry.dev/ai-videos/opus-5-5/nikolajankovic-616097)** (58 s · no hard cuts · no sound): “you're defi saver and explaining yourself in 1st person”  
  **Seen:** Runs at 12 frames per second, so it reads as real stop-motion. Pencil sketches of the loan numbers, a 3 a.m. price drop, a ratio thermometer; a taped paper strip at the bottom carries the first-person narration. Ends "Been doing this since 2019. Mostly at night."  
  **Borrow:** Let the product narrate itself, earnestly, in one strip of text. A lower frame rate sells a hand-made look.
- **[@KamStudioLabs](https://skillry.dev/ai-videos/opus-5-5/kamstudiolabs-877996)** (90 s · 0.1 cuts/10 s): “a bug that doesn't want to be fixed”  
  **Seen:** A glowing bug hides in lines of code and dodges a giant cursor; the punchline is a final status card: "WON'T FIX". It runs 90 s.  
  **Borrow:** End on a dry, literal label as the punchline. Play the absurd premise completely straight.
- **[@Gdgtify](https://skillry.dev/ai-videos/opus-5-5/gdgtify-929495)** (20 s · no hard cuts · no sound · square): “Words have assigned architectural roles.”  
  **Seen:** "WAIT" is huge from frame 0 with a small serif line under it. One line at a time, the words become the structure: WAITING hangs on cables, VOICE stands as columns, FLOOR is the platform. Loops back to WAIT. No sound.  
  **Borrow:** For copy-driven products, make the type the set. One line at a time, no illustrations.
- **[@ParkerRex](https://skillry.dev/ai-videos/opus-5-5/parkerrex-701462)** (18 s · no hard cuts · no sound · square): “every frame a pure function of time so my renderer can screenshot it”  
  **Seen:** One fixed diagram for 18 s; only its state changes (bucket level, counter, request log, step chart), and a one-line caption at the top names each phase. No sound, no hook drama.  
  **Borrow:** Hold the frame still and let only the numbers move. A plain caption line per phase is enough.

## `cinematic`

Trailer scale. A film genre or a famous ad as the frame, one recurring motif, a look that is part of the idea.

- **[@abhinayguptha](https://skillry.dev/ai-videos/opus-5-5/abhinayguptha-259981)** (20 s · 0.5 cuts/10 s): “a 20-second title sequence for a Netflix thriller that doesn't exist yet”  
  **Seen:** Black for half a second, then fingerprint contour lines fade up; credits in widely spaced serif, a map with a red route, a redacted case file stamped UNSOLVED, and a title drawn from the same lines. Mastered very loud (about -7 LUFS).  
  **Borrow:** One recurring motif from first frame to title. Bring the picture up faster than half a second, and mix to normal loudness.
- **[@1littlecoder](https://skillry.dev/ai-videos/opus-5-5/1littlecoder-378066)** (30 s · 1 cuts/10 s): “inspired by Apple 1984 ad, iykyk! avoid the border text or frames!”  
  **Seen:** A dark tunnel fades in, a Big-Brother face on a cinema screen with short captions ("ONE FEED."), an orange runner smashes the screen around 21 s, white-out, ends "Great minds don't think alike." No border text or frames.  
  **Borrow:** Homage to one famous ad gives a structure people already know. Keep the product's line for the very end.
- **[@jake11moran](https://skillry.dev/ai-videos/opus-5-5/jake11moran-414633)** (27 s · 1.5 cuts/10 s · no sound): “aim for half the speed you'd default to”  
  **Seen:** The opening line builds word by word over a painted wallpaper and is complete by 1.5 s. A spinning list lands on one item, windows pile onto a Mac desktop, the notch opens into the browser, ending on the name and "launching soon". No sound.  
  **Borrow:** Slow, eased camera moves over one desktop. A fast list that is texture, landing slowly on the line that matters.
- **[@johnsavage_ai](https://skillry.dev/ai-videos/opus-5-5/johnsavage-ai-427263)** (20 s · no hard cuts): “add film grain and CRT effect, make it mesmerizing”  
  **Seen:** The CRT is the idea, not a filter: the hook is a macro of RGB subpixels and a collapsing power-on scanline by 1.0 s, a channel label ("CH 05.5"), a head sliced into scanlines, the name with "Look closer.", and it ends back on the subpixels.  
  **Borrow:** Make the look part of the story (here, a TV switching on), not a layer on top.
- **[@advait_jayant](https://skillry.dev/ai-videos/opus-5-5/advait-jayant-712107)** (20 s · 4 cuts/10 s): “every frame and every sound written in code, no image or video models”  
  **Seen:** A red dot labelled "STATUS: CONTAINED" by 2 s, then the quoted line split into one huge condensed word per card, AI refusal messages stamped as a collage, a red card "OWNED BY NO ONE. OPEN TO EVERYONE.", ending on logo and the line.  
  **Borrow:** Split one sentence across cards, one huge word each, and let the last card land it.

## `app-store`

Feature by feature: one headline, one real screen, one claim per scene.

- **[@KmAsiff](https://skillry.dev/ai-videos/opus-5-5/kmasiff-549880)** (20 s · no hard cuts): “inspiration is yc videos and claude social videos”  
  **Seen:** "Stop bounces before you hit send." with the pain word struck through, complete by 1.0 s. Then one headline per scene beside a real-looking UI state (a score of 85/100, six result cards, a signup form catching a typo, a pricing checklist), ending on logo, URL and "5 free checks a day - no signup". 20 s, no hard cuts.  
  **Borrow:** Strike through the pain word in the hook. One headline and one UI state per scene; end on how to try it.
- **[@charlesmendez](https://skillry.dev/ai-videos/opus-5-5/charlesmendez-476517)** (57 s · no hard cuts): “with an example of a user creating a chatgpt ads campaign, then connecting their metrics”  
  **Seen:** "Your buyers now ask ChatGPT." stacked in huge type by 1.5 s, then each step as a headline on the left and a real-looking screen on the right (the answer, the journey, a voice agent, a phone follow-up, analytics). 57 s.  
  **Borrow:** Headline left, screen right, one step of one user's journey per scene. Cut the journey to 3-4 steps for 15-25 s.
- **[@Bilimfili1](https://skillry.dev/ai-videos/opus-5-5/bilimfili1-459762)** (50 s · no hard cuts · vertical): “each feature stays on screen for at least 2.5 seconds”  
  **Seen:** Vertical. "Let's see what's inside." with the app icon by 0.5 s. Each feature: a short title top-left, the phone screen, and the feature spilling out of the phone into a road below it. Ends on an App Store search bar with the app's name.  
  **Borrow:** Let each feature break out of the phone into the world. End on what the viewer types to find it.
- **[@felipemoller](https://skillry.dev/ai-videos/opus-5-5/felipemoller-936736)** (30 s · no hard cuts · vertical): “Quero que simule os gastos em estabelecimentos do dia a dia” (“I want it to simulate spending at everyday places”)  
  **Seen:** Vertical. A round isometric diorama of a supermarket assembles by 1.0 s. Each place gets a diorama with the app's real input under it: a voice waveform, a receipt photo, a typed entry. Ends "Gastou? Lancou." ("Spent it? Logged it.") with a button.  
  **Borrow:** One small scene per place the product is used, each paired with how you use it there.
- **[@deifosv](https://skillry.dev/ai-videos/opus-5-5/deifosv-786581)** (30 s · 7.3 cuts/10 s): “showing live stats from the website, show that users can play on desktop and mobile and multiple themes”  
  **Seen:** A live counter climbs from 0 to 5,699 "GAMES PLAYED" over real game footage, complete by 1.0 s. Then "NO DOWNLOAD. NO INSTALL. NO SIGN-UP.", a phone card, one court per city, ending on a "PLAY FREE NOW" button. About 7 cuts per 10 s.  
  **Borrow:** A live counter is an instant hook. Keep the real product running behind every card.
- **[@alex_prompter](https://skillry.dev/ai-videos/opus-5-5/alex-prompter-997524)** (34 s · no hard cuts · no sound): “The customer's problem, what I do, how it works in 3 steps, one proof point, and my name at the end”  
  **Seen:** Follows the five-scene structure exactly (problem, what it is, three numbered steps, "1,697+ subscribers.", name), but opens by typing the prompt into a chat box, which is about the making, not the product. No sound.  
  **Borrow:** The five-scene structure fits any product with a clear job. Open on the problem, not on how the video was made.

---

_Generated by `tools/brag-inspiration/build.py` in [awesome-opus5-5-videos](https://github.com/lalaee/awesome-opus5-5-videos) from notes written while watching each video. Videos and prompts belong to their creators; quotes are short excerpts, linked to each original._
