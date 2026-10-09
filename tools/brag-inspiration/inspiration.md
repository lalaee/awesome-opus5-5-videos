# Inspiration: launch videos that worked

Real videos people made with Claude Opus 5.5 by having it write the animation as code (HTML, Canvas, SVG, WebGL), the same way /brag-slim works. Picked from the 513-video collection at [awesome-opus5-5-videos](https://github.com/lalaee/awesome-opus5-5-videos): only full prompts, mostly launch and product videos, grouped by /brag tone.

## How to use this file

- **When:** after you can answer the Step 1 questions, before you commit to an angle. Read the patterns below and the section for your tone; skim one neighbouring tone if the project sits between two.
- **Take ideas, not content.** Borrow structures, camera ideas, pacing, transitions and build techniques. Never borrow another project's copy, claims, numbers, brand or characters, and never mention these creators in the video.
- **One or two ideas per video.** The project still sets the angle. If nothing here fits, ignore it: specific beats borrowed.
- **The links are optional.** Each name opens the original next to a remake. Everything you need is written here, so the file works offline.

## Patterns that keep working

- **Hook in the first second.** The strongest briefs ask for it outright: "open with a striking hook in the first second" ([@reflex_cloud](https://skillry.dev/ai-videos/opus-5-5/reflex-cloud-304046)), "1s hook, loop" ([@ishaaqahamed](https://skillry.dev/ai-videos/opus-5-5/ishaaqahamed-107563)).
- **Loop it.** Make the last frame equal the first so it plays forever in a feed ([@annacher](https://skillry.dev/ai-videos/opus-5-5/annacher-433425), [@techhalla](https://skillry.dev/ai-videos/opus-5-5/techhalla-498547)).
- **Real material beats recreation.** "Use as much of the real website as possible" ([@wani_shola](https://skillry.dev/ai-videos/opus-5-5/wani-shola-459278)); "use assets from the current live site" ([@madebyjmayala](https://skillry.dev/ai-videos/opus-5-5/madebyjmayala-649220)); "Real UI. Real data. No placeholders." ([@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381)).
- **Every frame a pure function of time.** "every frame a pure function of time so my renderer can screenshot it" ([@parkerrex](https://skillry.dev/ai-videos/opus-5-5/parkerrex-701462)); capture frame by frame in headless Chrome, add motion blur, then ffmpeg ([@xelandre](https://skillry.dev/ai-videos/opus-5-5/xelandre-687413)).
- **Check stills before the full render.** "First render one frame per beat as a contact sheet. Fix anything cramped or broken" ([@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381)).
- **Slower reads as more expensive.** "aim for half the speed you'd default to" ([@jake11moran](https://skillry.dev/ai-videos/opus-5-5/jake11moran-414633)); motion blur on fast moves, gentle ease-in-out.
- **Works muted.** "The story must also work muted." ([@howdevelop](https://skillry.dev/ai-videos/opus-5-5/howdevelop-733090)). Most feeds autoplay without sound.
- **Avoid the AI giveaways.** "Avoid the frames and texts on the corners which are typical ai made giveaways" ([@souravbhar871](https://skillry.dev/ai-videos/opus-5-5/souravbhar871-477361)): no corner labels, timecodes, fake HUD borders or frame-within-frame chrome unless the product has them.
- **Cut to the music.** "every cut, animation hit, and scene change lands on a beat or drop" ([@jhylee95](https://skillry.dev/ai-videos/opus-5-5/jhylee95-452427)).

## What went wrong, and the fix

- **Too fast, not professional, bad music.** One creator's follow-up after the first pass: "it is a bit too fast and bumpy", "This is not a professional-looking video", and "can you choose a royalty-free song online? You are clearly not a good song maker." ([@sachaarbonel](https://skillry.dev/ai-videos/opus-5-5/sachaarbonel-673648)). Fix: hold readable text long enough, smooth the transitions, and mix the music properly or use a real track.
- **No video at the end.** "where is the video? I only see a config file" (translated from German, [@iammxfschr](https://skillry.dev/ai-videos/opus-5-5/iammxfschr-955831)). Fix: always render and hand over the MP4.
- **Generic showreels.** 41 videos in the collection come from one prompt ("make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are…"). They're impressive, but they look alike because the prompt has no product in it. /brag's whole job is the opposite: specific to one project.

## `default`

Punchy, playful, clean. Small stories and one clear flow.

- **[@hqmank](https://skillry.dev/ai-videos/opus-5-5/hqmank-241156)** (canvas · svg · gsap): “like it's the hero video on its GitHub README”  
  Name where the video will live; it sets length, framing and loop. The project's own three-beat tagline ('Give a site. Write a goal. Jev clicks.') was already the storyboard.
- **[@jackfriks](https://skillry.dev/ai-videos/opus-5-5/jackfriks-338762)** (canvas · svg · gsap): “use the pig assets on new branch of lovelee to make a 9:16 short story animation”  
  A tiny story starring the project's own characters and assets, with the app teased only at the end. Works when the product has a mascot or illustrations.
- **[@mattbean](https://skillry.dev/ai-videos/opus-5-5/mattbean-917572)** (canvas): “1. connect your agent 2. your agent fills out your listing and sets up redemption 3. go live!”  
  When the product is a three-step flow, the three steps are the three highlights. Nothing else needed.
- **[@justincooperman](https://skillry.dev/ai-videos/opus-5-5/justincooperman-188876)** (canvas · css): “users ask for branded images and see them added to content”  
  Show the output landing in its real context (the post, the page), not floating on a gradient.
- **[@VisheshBaghell](https://skillry.dev/ai-videos/opus-5-5/visheshbaghell-119508)** (svg · gsap): “build me a product demo for my site using /brag skill. make sure to emphasize on all features”  
  A /brag run in the wild. Note the ask was 'all features'; still pick the 2-3 that carry the story and let the rest go.

## `polished`

Serious and restrained. Continuity, real UI, long holds.

- **[@AnnaCher___](https://skillry.dev/ai-videos/opus-5-5/annacher-433425)** (svg): “build a product promo from our own UI, not generic components”  
  One element that never cuts: it morphs from state to state, driven by a cursor with real clicks and drags, the camera zooming so each state fills the frame, last frame equal to the first so it loops. Everything computed in seek(t). Adapted from @twoclipping's widely remixed UI-states prompt.
- **[@verbove](https://skillry.dev/ai-videos/opus-5-5/verbove-268381)** (canvas): “Content enters after its container starts morphing and leaves before the next morph so text never overlaps”  
  The fix for muddy transitions, plus 'Real UI. Real data. No placeholders.' and 'First render one frame per beat as a contact sheet' before the full render.
- **[@HowDevelop](https://skillry.dev/ai-videos/opus-5-5/howdevelop-733090)** (canvas): “The story must also work muted.”  
  Premium developer-tool launch film: exactly 15s, important content kept inside a 9:16-safe centre so one render crops to every platform, sound that resolves on the final frame.
- **[@dale_vaz](https://skillry.dev/ai-videos/opus-5-5/dale-vaz-879074)** (canvas): “start with a single dot on a black screen and then have multiple windows show up”  
  A scale journey for dense, multi-panel products: dot to full desktop, zoom out until it is a point in space, back in on mobile, end on the one-line promise.
- **[@wani_shola](https://skillry.dev/ai-videos/opus-5-5/wani-shola-459278)** (svg · gsap): “Use only facts and numbers that are on the site.”  
  Premium brand rules in one list: three colours and the site's own fonts, one idea per shot, key objects centred, eased motion only, cut on the beat.

## `yc-parody`

The startup-launch genre that yc-parody plays straight. Learn the conventions so you can deliver them with a straight face.

- **[@moritzkremb](https://skillry.dev/ai-videos/opus-5-5/moritzkremb-466494)** (svg · gsap): “very professionally edited, motion-graphics-styled product launch videos that you see people making on Twitter”  
  The reference genre itself; 8 videos in the collection start from this prompt. Feature, benefit, feature, logo, all with real assets. Deliver these conventions dead straight and the parody does itself.
- **[@deedydas](https://skillry.dev/ai-videos/opus-5-5/deedydas-252537)** (svg · gsap): “make a modern slick and punchy video for a modern startup that works on inference”  
  Fifteen words that two other creators reused in their own prompts. When the register is clear (slick, punchy, modern startup) the brief can be tiny; spend the effort on the claim, not the adjectives.
- **[@viktoroddy](https://skillry.dev/ai-videos/opus-5-5/viktoroddy-402509)** (canvas · svg · gsap · css): “just hit 1 million monthly visitors after 8 months after launch”  
  One milestone number as the spine of the whole video. Only use it if the project actually states it.
- **[@KmAsiff](https://skillry.dev/ai-videos/opus-5-5/kmasiff-549880)** (svg): “inspiration is yc videos and claude social videos”  
  Naming the genre you are imitating does more than a list of adjectives.

## `chaotic`

Fast and loud, but still edited. The good ones lock the message and make the frame go wild.

- **[@techhalla](https://skillry.dev/ai-videos/opus-5-5/techhalla-498547)** (canvas): “Magenta/green may misregister (print offset) by 2–4px on impact frames only.”  
  Chaos with rules: a locked six-line message in exact order, a strict three-colour palette, three typefaces with fixed jobs, glitches only on impact frames, a 'STOP SCROLLING' cold open, and a loop.
- **[@kloss_xyz](https://skillry.dev/ai-videos/opus-5-5/kloss-xyz-941143)** (canvas · audio): “chaotic brain rot video with excellent motion + sound design”  
  Chaotic still needs a real mix. Vertical, relentless, but the sound is designed, not stacked.
- **[@supremebeme](https://skillry.dev/ai-videos/opus-5-5/supremebeme-306746)** (svg): “make a brainrot video about the terminal. i can't escape it.”  
  The chaos comes from a relatable confession about the product, not from random effects.
- **[@maxalexweber](https://skillry.dev/ai-videos/opus-5-5/maxalexweber-459784)** (canvas · svg): “Make a ODATANO edit that goes hard”  
  The fan-edit format: hard beat cuts, flash frames, speed ramps, the product as the subject of the edit.
- **[@robvjourney](https://skillry.dev/ai-videos/opus-5-5/robvjourney-237474)** (canvas · svg): “Go ALL OUT and make the most badass video you possibly can”  
  Fifteen seconds of a live site at maximum energy. Pair this energy with the site's real copy and visuals or it turns generic.

## `deadpan`

Calm, dry, text-forward. The premise is the joke; the delivery never winks.

- **[@KamStudioLabs](https://skillry.dev/ai-videos/opus-5-5/kamstudiolabs-100086)** (canvas · audio): “a 45-second silent short film with no dialogue, where sound tells half the story”  
  Let sound land the jokes so the picture can stay still and straight-faced.
- **[@_nikolajankovic](https://skillry.dev/ai-videos/opus-5-5/nikolajankovic-616097)** (canvas): “you're defi saver and explaining yourself in 1st person”  
  The product narrates itself, earnestly, in first person. Hand-drawn stop-motion keeps it humble.
- **[@KamStudioLabs](https://skillry.dev/ai-videos/opus-5-5/kamstudiolabs-877996)** (canvas · particles): “a bug that doesn't want to be fixed”  
  A one-line absurd premise played completely straight. The humor is in the premise, never in the delivery.
- **[@Gdgtify](https://skillry.dev/ai-videos/opus-5-5/gdgtify-929495)** (canvas): “Words have assigned architectural roles.”  
  Text-forward done right: one line at a time, the type itself becomes the set, and the final line stands on what earlier words built. Good for copy-driven products.

## `cinematic`

Trailer scale. Borrow a film genre or a famous ad, then add a finishing layer.

- **[@abhinayguptha](https://skillry.dev/ai-videos/opus-5-5/abhinayguptha-259981)** (shader · webgl · canvas): “a 20-second title sequence for a Netflix thriller that doesn't exist yet”  
  Frame the product as a title sequence: credits-style type, slow reveals, one recurring motif.
- **[@1littlecoder](https://skillry.dev/ai-videos/opus-5-5/1littlecoder-378066)** (canvas): “inspired by Apple 1984 ad, iykyk! avoid the border text or frames!”  
  Homage to a famous ad gives instant structure and stakes. Also: no border text or frames, a common AI giveaway.
- **[@jake11moran](https://skillry.dev/ai-videos/opus-5-5/jake11moran-414633)** (canvas · svg · gsap · ai-image): “aim for half the speed you'd default to”  
  One continuous camera over one desktop, no hard cuts, 1.5-3s eased moves, motion blur and light grain. A spinning list that is texture, not text, then lands slowly on the one that matters.
- **[@johnsavage_ai](https://skillry.dev/ai-videos/opus-5-5/johnsavage-ai-427263)** (threejs · shader · canvas): “add film grain and CRT effect, make it mesmerizing”  
  A finishing layer (grain, CRT, halation) turns clean motion into a look. Apply it last, over everything, and keep text legible through it.
- **[@advait_jayant](https://skillry.dev/ai-videos/opus-5-5/advait-jayant-712107)** (canvas): “every frame and every sound written in code, no image or video models”  
  A manifesto built on one quoted line. All visuals and sound generated in code, which is exactly the /brag-slim setup.

## `app-store`

Feature-by-feature, real screens, clear user flow.

- **[@Bilimfili1](https://skillry.dev/ai-videos/opus-5-5/bilimfili1-459762)** (canvas · svg): “each feature stays on screen for at least 2.5 seconds”  
  Real recordings, not mocks; every number on screen comes from them; text kept clear of the TikTok/Instagram UI; each feature breaks out of the phone into the world around it.
- **[@charlesmendez](https://skillry.dev/ai-videos/opus-5-5/charlesmendez-476517)** (canvas · svg · gsap): “with an example of a user creating a chatgpt ads campaign, then connecting their metrics”  
  One user's journey chained end to end. Each step is a scene, and the chain itself shows the product's range.
- **[@alex_prompter](https://skillry.dev/ai-videos/opus-5-5/alex-prompter-997524)** (svg · gsap): “The customer's problem, what I do, how it works in 3 steps, one proof point, and my name at the end”  
  A five-scene structure that fits any product with a clear job to do.
- **[@felipemoller](https://skillry.dev/ai-videos/opus-5-5/felipemoller-936736)** (threejs · svg · gsap): “Quero que simule os gastos em estabelecimentos do dia a dia” (“I want it to simulate spending at everyday places”)  
  Simulate the product in its real-world setting (supermarket, gas station, restaurant) so each feature arrives as a moment from daily life. Vertical.
- **[@deifosv](https://skillry.dev/ai-videos/opus-5-5/deifosv-786581)** (canvas · gsap · css): “showing live stats from the website, show that users can play on desktop and mobile and multiple themes”  
  Real stats plus platform and theme range as quick, clean cards.

---

_Generated by `tools/brag-inspiration/build.py` in [awesome-opus5-5-videos](https://github.com/lalaee/awesome-opus5-5-videos). Videos and prompts belong to their creators; quotes are short excerpts, linked to each original._
