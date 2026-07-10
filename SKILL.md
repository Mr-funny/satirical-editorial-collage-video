---
name: broll-shot-builder
description: Build stylized B-roll production plans from concepts or pasted scripts by reading the text, selecting a visualizable excerpt, mapping it to metaphors, then producing first-frame prompts, tail-frame prompts, and animation prompts for GPT/Nano Banana image generation plus Seedance/Grok first-tail-frame video generation. Use when Codex needs script-to-B-roll workflows,首尾帧 animation logic, reference-to-video prompts, retro editorial/collage motion, staged entrances/exits/transformations, or assembly plans for short social/video B-roll.
---

# B-roll Shot Builder

## Core Pattern

Convert a pasted script, argument, or single long-shot idea into a chain of short clips. Each clip must be planned as a **first frame -> tail frame -> animation prompt** unit. The first frame is sparse, the tail frame is the intended final composition, and the animation prompt controls how the video travels between them.

Use three layers of rhythm:

1. **Text-to-metaphor rhythm:** read the script, choose a compact excerpt, identify conflict/irony, and choose one visible metaphor.
2. **Frame rhythm:** write one prompt for the sparse first frame and one prompt for the fuller tail frame.
3. **Inside-clip rhythm:** write a 6-second micro-timeline that gets from the first frame to the tail frame through ordered beats: hold blank stage, pop in prop, add doors/characters/icons, transform objects, then settle.

Prefer clear staged changes over busy all-at-once prompts. Keep camera, palette, typography, and background consistent across clips. Lock already-visible elements unless that element is the named thing changing.

Start sparse. Do not generate a fully populated first frame when the intended animation is staged. A strong first frame usually contains only the locked background, text/label, and maybe one anchor prop. The tail frame may be full and specific. Let the video add the main metaphor, character, icons, labels, or choice paths one by one. Start motion only after the relevant elements have appeared and settled.

Supported visual changes:

- **Entrance:** an element appears, pops in, slides in, unfolds, drops, or is stamped onto the scene.
- **Exit:** an element leaves, fades, peels off, gets crossed out, dissolves, or is lifted away.
- **Transformation:** an existing element changes shape, color, label, state, scale, direction, or function.
- **Replacement:** one symbol turns into another, such as a rigid blueprint becoming an open grid.
- **Relationship change:** lines connect/disconnect, chains loosen, gates open, arrows reroute, or competing paths appear.
- **Motion/state change:** a still object begins rotating, a locked object unlocks, a red stamp becomes a neutral scale, or a closed system becomes an open platform.

## Workflow

1. If the user provides a long script or pasted argument, select a compact excerpt with high visual metaphor potential. Prefer one thesis, contrast, or turning point over trying to cover the whole text.
2. Think before prompting. Rewrite the excerpt as a B-roll premise: `abstract idea -> emotional temperature -> conflict/irony -> visible metaphor -> staged visual changes`.
3. Extract the target format, duration, tools, and available reference images/video.
4. Choose the panel color from the text emotion. Do not default to a green board. Use color as narrative pressure: green for analytical control, red/coral for anger or alarm, yellow/mustard for irony, blue/gray for distance or melancholy, black/cream for bureaucracy or menace.
5. Identify stable elements, first-frame elements, tail-frame elements, entering elements, exiting elements, transforming elements, relationship changes, and motion-only elements.
6. Create a clip chain where each clip has:
   - `first_frame_prompt`: sparse starting image
   - `tail_frame_prompt`: full intended final image
   - `animation_prompt`: first-to-tail motion instructions
7. For each clip, write:
   - selected excerpt and reasoning
   - emotion, palette, and panel color rationale
   - first-frame image prompt for GPT/Nano Banana
   - tail-frame image prompt for GPT/Nano Banana
   - reference-to-video animation prompt for Grok/Seedance
   - negative prompt
   - continuity notes
   - assembly timing and transition notes
8. Generate images first. Use GPT/Nano Banana to create the first frame and tail frame. Then use Grok/Seedance with both frames when the tool supports first/tail references.
9. If the user has local image and video tools, produce tool-ready prompts and command placeholders instead of assuming exact CLI flags.
10. Add sound design notes when useful: for this style, favor retro jazz percussion, light clock ticks, brushed drums, tape warmth, and tight stingers on element entrances, exits, or transformations.

## First/Tail Frame Logic

Prefer first/tail-frame generation for serious B-roll because it separates composition from motion:

- **First frame prompt:** describe the blank or sparse stage. Include exact aspect ratio, background, label text, paper texture, and empty space. Explicitly exclude final elements.
- **Tail frame prompt:** describe the final composition with all important elements present. This is where visual certainty comes from.
- **Animation prompt:** describe how to move from first to tail. It should reference both images and impose a timeline. The model should not invent a new final layout.

Template:

```text
Text excerpt: [chosen sentence or phrase]
Thesis: [what the viewer should understand]
Conflict/Irony: [what makes it visual]
Metaphor: [paper-collage scene]

First frame prompt:
[sparse stage, exact text, empty zones, avoid final elements]

Tail frame prompt:
[full final composition, exact final elements, same style/camera/palette]

Animation prompt:
Use image 1 as the exact first frame and image 2 as the target tail frame.
Do not start from image 2. Do not crossfade. Do not morph the whole image at once.
0.0-0.6s: hold first frame.
0.6-1.6s: first major sticker enters.
1.6-2.6s: second group enters.
2.6-3.8s: characters or secondary props enter.
3.8-4.8s: icons/question marks/relationship lines enter.
4.8-5.5s: small details and shadows settle.
5.5-6.0s: hold stable tail frame close to image 2.
```

## Generation Methods

Use methods deliberately:

- **`image_to_video`:** use one sparse first frame. Best when the clip should discover/construct the scene through motion. Risk: the model may invent or drift the final elements.
- **First/tail `reference_to_video`:** use a sparse first frame plus a fuller tail frame. Best when the final composition must include specific objects, icons, or layout. Risk: the model may jump toward the tail too quickly; reduce this with a sparse first frame and strict timeline.
- **Single final reference assembly:** use only one complete final reference image semantically. Tell the model to treat it as the element list, style guide, and final composition only, while the video itself begins from a blank paper stage. Use this when two different reference images cause interpolation/jump cuts or cost too much.

When uncertain, run both methods with the same premise and compare extracted frames. For first/tail `reference_to_video`, explicitly say `use image 1 as the exact first frame and image 2 as the target tail frame; do not reveal the full tail before the final second`.

For single final reference assembly, use this instruction shape:

```text
Use the reference image only as the final target composition, element inventory, and style guide.
Do not start from the reference image.
The video must begin with a blank [paper/background] stage: no [main prop], no [secondary props], no people, no icons.
Assemble the reference image gradually as stop-motion paper stickers.
Do not crossfade. Do not morph the whole reference image in at once. Do not reveal the full composition before the final second.
```

If a local video tool requires at least two image entries for `reference_to_video`, pass the same final reference image twice and state that there is only one unique reference image. This satisfies the tool schema while preserving the single-reference method. Verify with extracted frames, because some models may still start from the reference image despite the prompt.

## Script-to-B-roll Selection

For pasted prose, do not visualize every sentence. Pick a short segment that can be shown as motion. Good candidates include:

- a binary contrast: freedom vs coercion, fixed blueprint vs open choice, pilgrim vs wanderer
- a causal turn: force replaces choice, rights are discovered, a closed family rule becomes a boundary-respecting relationship
- a vivid abstraction: Leviathan, natural rights, liquid modernity, exit right, minimum state

Convert the excerpt into a visual grammar:

```text
Excerpt: [one or two sentences]
Thesis: [what the viewer should feel/understand]
Emotion: [anger, irony, anxiety, restraint, melancholy, bureaucracy, absurdity, etc.]
Palette: [panel color + accent colors chosen from the emotion]
Metaphor: [visible scene]
Stable frame: [what must not change]
Change beats: [entrance, exit, transformation, relationship change, motion/state change]
Final tail frame: [stable state for continuation]
```

## Emotion-Led Color Choice

Choose the background/panel color after reading the excerpt. The panel should support the idea, not repeat a fixed house style.

- **Analytical restraint / self-control:** muted green, chalkboard green, off-white paper, black ink, small red accents.
- **Anger / alarm / emotional heat:** deep red, faded crimson, rust, charcoal, off-white paper, black ink.
- **Satire / irony / absurd instruction:** mustard yellow, nicotine beige, faded coral, black ink, small teal accents.
- **Melancholy / alienation / distance:** blue-gray, cold slate, dirty white, pale cyan accents.
- **Bureaucracy / coercion / institutional menace:** cream paper, black, gray, stamped red, file-folder tan.
- **Hope / release / opening choice:** pale blue or softened green with warmer cream and one bright exit accent.

When the text has mixed emotions, let the background carry the dominant emotion and reserve the accent color for the counterforce. Example: red panel for anger, off-white paper labels for rational observation, black dotted lines for repetitive thought.

## Grok CLI Video Trigger

On this user's machine, prefer `/Users/huangweihong/.grok/bin/grok` when it exists. The Grok CLI is a Grok Build agent, not a simple `grok-video` binary. Trigger video generation by running `grok -p` with a prompt that explicitly tells Grok to use its media generation capability, preferably first/tail `reference_to_video` when two generated frames exist, then save or copy the generated mp4 to the requested shot path.

Use this shape for each shot after its still image exists:

```bash
export HTTPS_PROXY=socks5h://127.0.0.1:10808
export HTTP_PROXY="$HTTPS_PROXY"
export ALL_PROXY="$HTTPS_PROXY"

/Users/huangweihong/.grok/bin/grok \
  --prompt-file grok_prompts/shot_01.md \
  --cwd "$(pwd)" \
  --permission-mode bypassPermissions \
  --max-turns 8 \
  --output-format plain
```

The generated video may first appear under `~/.grok/sessions/.../videos/1.mp4`; the prompt must tell Grok to copy it to `shot_01.mp4`. Run Grok with the proxy environment above by default. Override the proxy with `BROLL_GROK_PROXY` only when a different local proxy endpoint is needed.

For tail-frame chaining after a generated clip, extract the real tail frame from the main video stream, not a QuickLook thumbnail:

```bash
ffmpeg -y -sseof -0.08 -i clip_01.mp4 -map 0:v:0 -frames:v 1 tail_01.png
```

If the MP4 includes an attached picture stream, `-map 0:v:0` prevents accidentally extracting the cover image.

## Planning Script

Use `scripts/build_broll_plan.py` when the user wants a reusable plan or batchable prompts.

Minimal example:

```bash
python3 scripts/build_broll_plan.py \
  --concept "a woman running inside a hamster wheel while productivity icons float in" \
  --elements "background+title,hamster wheel,woman runner,icons" \
  --style "retro editorial collage, warm paper texture, jazz percussion, clock tick rhythm" \
  --out ./out/productivity-wheel
```

The script writes `shot_plan.json`, `prompts.md`, `assemble_manifest.json`, `cli_commands.sh`, and per-shot Grok prompts under `grok_prompts/`.

## Reference Use

Read `references/style-and-staging.md` when you need more detailed shot grammar, style recipes, or prompt patterns. Use it especially for:

- recreating the retro Nano Banana + Seedance-style B-roll described by the user
- deciding how to split complex compositions into additive shots
- adapting prompts for local GPT image generation and Grok/Seedance-style video generation

## Quality Rules

- For very short clips, keep one narrative change per shot. For 6-second Grok clips, use a micro-timeline with several ordered changes if the background and existing elements can remain locked.
- Do not regenerate the whole scene with unrelated composition changes between shots.
- Repeat exact wording for persistent art direction, aspect ratio, camera, character identity, typography style, and palette.
- Make each image prompt describe a complete final frame for that shot, not only the new element.
- Make each video prompt describe motion from the previous shot state to the current shot state.
- In Grok prompts, include explicit timing beats such as `0.0-0.8s hold`, `0.8-2.0s prop enters`, `2.0-3.2s settle`, `3.2-4.4s character enters`, `4.4-6.0s motion/icons`.
- Favor 6-second Grok clips when the tool's minimum duration is 6 seconds; trim only during assembly if the user wants a shorter final piece.
- End with an assembly plan that names clip order, durations, transitions, and audio cues.
