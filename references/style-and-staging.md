# Style And Staging Reference

## Staged Entrance Grammar

Use this sequence when recreating the reference logic:

| Beat | Purpose | Visual change | Motion |
| --- | --- | --- | --- |
| 1 | Establish context | background, headline, framing | paper texture drift only; keep camera locked |
| 2 | Reveal metaphor | main prop/object | pop-in, slide, bounce, mechanical tick |
| 3 | Shift meaning | prop/object changes state | label changes, chain loosens, stamp fades, lock opens, blueprint becomes grid |
| 4 | Human action | character or choice path | enter frame, exit frame, split into alternatives, start looped action |
| 5 | Data/callouts | icons, labels, symbols, relationship lines | one-by-one float, orbit, connect, disconnect, tick-synced entrance |
| 6 | Optional payoff | full composition | cohesive loop, final accent, title beat |

The key is not the exact objects. The key is sequencing visible ideas while preserving everything already established.

For 1-3 second clips, use one major visible change. For Grok/Seedance 6-second image-to-video clips, use a micro-timeline with multiple ordered beats inside the same clip. Example:

```text
0.0-0.8s: hold the source frame steady; paper grain flickers subtly.
0.8-2.0s: main prop sticker pops/slides into place.
2.0-3.2s: prop transforms or changes state while staying anchored.
3.2-4.4s: a character, choice path, label, or counter-symbol enters/exits.
4.4-6.0s: relationship lines, icons, or secondary states settle into a stable final meaning.
```

## Sparse First Frame Rule

Use a sparse first frame when the clip's point is staged appearance. This is the image 1 prompt in a first/tail workflow. Include only:

- locked paper panel/background
- core label or title
- one anchor object if needed for scale
- generous empty space where the metaphor will assemble

Do not include the full cast of props, icons, characters, and final relationship lines in the first frame. Generate a separate full tail frame prompt for the final composition.

Recommended 6-second rhythm:

```text
0.0-0.6s: sparse first frame remains clean; no final elements visible yet.
0.6-1.8s: first major element enters and settles.
1.8-3.0s: second major element enters or first element transforms.
3.0-4.4s: relationship/action begins.
4.4-5.4s: secondary icons or labels enter.
5.4-6.0s: hold a stable readable tail frame.
```

## First/Tail Frame Workflow

Default to first/tail planning for B-roll:

1. Read the script.
2. Select one visualizable excerpt.
3. Convert the excerpt into a conflict or metaphor.
4. Write a sparse first-frame prompt.
5. Write a full tail-frame prompt.
6. Write a first-to-tail animation prompt that controls the middle.
7. Generate both images with GPT/Nano Banana.
8. Generate video with Grok/Seedance using first/tail references.
9. Extract 1fps frames and the real tail frame to validate continuity.

Prompt roles:

- **First frame:** controls where the video starts. It should be blank or sparse.
- **Tail frame:** controls final composition and element identity.
- **Animation prompt:** controls timing and prevents instant interpolation.

For A/B comparisons, compare first/tail `reference_to_video` against `image_to_video`:

- Use the same sparse first frame for both methods.
- Use the same motion timeline.
- For first/tail `reference_to_video`, add a tail frame showing the intended final composition.
- Evaluate by extracting frames at 1fps and comparing whether elements enter gradually, whether the first second stays sparse, and whether the final state is complete.

First/tail animation prompt skeleton:

```text
Use image 1 as the exact first frame and image 2 as the target tail frame.
Preserve camera, paper background, palette, typography, sticker outlines, and lighting.
Do not start from image 2.
Do not crossfade from image 1 to image 2.
Do not morph the whole image at once.
Do not reveal the full tail composition early.

0.0-0.6s: hold image 1 nearly unchanged.
0.6-1.6s: first major sticker enters.
1.6-2.6s: primary prop group enters one by one.
2.6-3.8s: character group enters one by one.
3.8-4.8s: icons, labels, question marks, arrows, or relationship lines enter.
4.8-5.5s: small details, shadows, and jitter settle.
5.5-6.0s: hold a stable final frame close to image 2.
```

## Single Final Reference Assembly

Use this when two reference images cause jumpy interpolation or cost too much. Provide only one complete final reference image. Treat it as the element inventory, final layout, and style guide, not the starting frame.

Prompt requirements:

- The video must begin from a blank paper stage that is described in text.
- The reference image must not be visible at the start.
- Elements from the reference enter by group: main machine, doors/props, people, question marks/icons, then small details.
- The last second should settle close to the reference image.
- Explicitly forbid crossfade, whole-image morphing, early reveal, and a fully populated first frame.

Recommended timing:

```text
0.0-0.6s: blank paper stage, only paper texture and optional bottom label.
0.6-1.6s: main machine or central metaphor sticker pops into place.
1.6-2.6s: primary props enter one by one.
2.6-3.8s: characters enter one by one.
3.8-4.8s: question marks, personal icons, arrows, or relationship symbols enter.
4.8-5.5s: small details, shadows, roller/stamp, and jitter settle.
5.5-6.0s: hold final composition close to the reference.
```

## Change Types

Use more than entrances. Choose the change type that matches the script:

- **Entrance:** new symbol appears.
- **Exit:** old symbol leaves, peels away, fades, or is crossed out.
- **Transformation:** one element stays in place but changes meaning: blueprint to open grid, red stamp to neutral scale, chain to dotted boundary.
- **Replacement:** old sticker is swapped for a new sticker in the same position.
- **Relationship change:** arrows reroute, boundaries appear, lines connect/disconnect, exits open.
- **State/motion change:** still wheel starts spinning, closed gate opens, fixed map becomes branching paths.

## Retro Editorial Motion Look

Use this look when the user mentions the reference style:

- flat editorial illustration mixed with soft 3D paper cutout depth
- warm off-white paper grain, emotion-led panel color, black ink accents, one or two sharp accent colors
- single paper panel or vintage editorial layout, large clean headline, simple geometric composition
- gentle halftone, risograph texture, imperfect ink edges
- kinetic collage motion: pop, slide, float, bob, rotate, snap
- tactile props with clear silhouette
- no photorealistic skin, no glossy corporate gradients, no cluttered background

## Emotion-Led Palette Recipes

Select the panel color from the excerpt before writing image prompts. Use the same palette in first frame, tail frame, and video prompt.

| Text emotion | Panel / background | Accents | Use for |
| --- | --- | --- | --- |
| restrained analysis | muted chalk green | off-white paper, black ink, small red | thinking, control, observation, time |
| anger or threat | deep crimson, rust red | charcoal, off-white, hot red flame | rage, alarm, conflict, emotional heat |
| satire or absurdity | mustard yellow, nicotine beige | black ink, coral, teal | mockery, irony, social commentary |
| alienation or melancholy | blue-gray, cold slate | pale cyan, dirty white | loneliness, distance, meaning loss |
| bureaucracy or coercion | cream file paper, gray | black stamps, institutional red | rules, force, systems, Leviathan |
| release or choice | softened green or pale blue | bright exit color, cream | opening, freedom, paths, recovery |

Do not reuse green by habit. If the script's dominant feeling is anger, heat, coercion, or danger, a red/rust/charcoal board may be more truthful. If the excerpt is reflective or clinical, green can work because it reads as a thinking surface.

## Prompt Skeletons

First-frame image prompt:

```text
Create a sparse [aspect ratio] first frame for a short B-roll animation.
Scene: [blank/sparse starting state].
Persistent style: [style string repeated verbatim].
Emotion and palette: [dominant emotion, panel color, accent colors, why].
Composition: [camera/framing/layout].
Visible elements: [background, label, optional anchor object only].
Text: [exact text if any], clean readable typography.
Lighting/color: [palette].
Avoid: no [tail-frame elements], no characters, no icons, no relationship lines, no style drift.
```

Tail-frame image prompt:

```text
Create the full [aspect ratio] tail frame for the same B-roll animation.
Scene: [complete final metaphor state].
Persistent style: [same style string repeated verbatim].
Emotion and palette: [same dominant emotion, same panel color, same accents].
Composition: [same camera/framing/layout].
Final elements: [main prop, characters, icons, labels, relationship lines].
Text: [exact text if any], clean readable typography.
Lighting/color: [same palette].
Avoid: no alternate style, no unrelated objects, no unreadable text.
```

Video prompt:

```text
Animate from image 1, the first frame, toward image 2, the tail frame, over [duration].
Keep camera, background, typography, shadows, and sticker style consistent.
Micro-timeline:
[0.0-0.8s hold/stabilize]
[0.8-2.0s first visible change: entrance/exit/transformation]
[2.0-3.2s settle or state change]
[3.2-4.4s next visible change: relationship, replacement, label, or character action]
[4.4-6.0s loop/action/icons/final stable meaning]
Stability rules: no scene reset, no layout redesign, no unintended text changes, no camera movement, no crossfade, no whole-image morph.
End on a stable frame close to image 2.
```

Negative prompt:

```text
photorealism, busy background, unreadable text, extra limbs, extra characters,
logo artifacts, random UI, warped typography, camera angle change, style drift,
flicker, sudden object replacement
```

## Splitting Rules

- If an element can be named as a noun phrase, it can usually become its own shot.
- If a change can be named as a verb phrase, it can usually become its own beat: lock opens, stamp fades, map branches, chain loosens, label changes.
- If two elements must appear together to be understood, keep them together as one shot.
- If an element has a complex entrance, split it into "appears" and "starts motion".
- If an element has a meaningful transformation, keep the element anchored and describe exactly what changes.
- Keep typography in Shot 1 unless the text itself is the reveal.
- Make icons enter as an ordered group only when there are more than five; otherwise list individual entry beats.
- If the video tool returns 6-second clips, combine compatible adjacent beats into one clip instead of wasting the duration on a single pop-in.
- Do not combine beats that require a different source image, a different camera layout, or a large identity change that tends to cause regeneration drift.
- Always plan the clip's final second as a stable tail frame, even if motion continues earlier.

## Local Tool Adaptation

For local GPT image generation:

- Use the image prompt as the main prompt.
- If a previous shot image exists, pass it as reference when the local tool supports image-to-image.
- Generate at the final video aspect ratio.
- Save outputs as `shot_01.png`, `shot_02.png`, etc.

For Grok/Seedance-style video generation:

- Use the first shot still or the previous clip's extracted tail frame as the single image reference.
- Use the video prompt as the motion instruction.
- For 6-second clips, include a detailed micro-timeline and stability rules.
- If exact final composition matters, create both a sparse first frame and a full tail frame, then use first/tail `reference_to_video`.
- If comparing methods, create both an `image_to_video` prompt and a first/tail `reference_to_video` prompt.
- If using single final reference assembly, pass only the full final image to `reference_to_video` and describe the blank starting stage in the prompt.
- Save outputs as `shot_01.mp4`, `shot_02.mp4`, etc.
- For this user's Grok CLI, always start Grok with the proxy environment by default: `HTTPS_PROXY=socks5h://127.0.0.1:10808`, `HTTP_PROXY=$HTTPS_PROXY`, and `ALL_PROXY=$HTTPS_PROXY`. Then call `/Users/huangweihong/.grok/bin/grok --prompt-file grok_prompts/shot_01.md --cwd "$(pwd)" --permission-mode bypassPermissions --max-turns 8 --output-format plain`.
- Grok Build's media path is agent-tool based: it calls `image_to_video` internally and may save first to `~/.grok/sessions/.../videos/1.mp4`; prompt it to copy the mp4 to the requested shot filename.
- If chaining clips, extract the real tail frame with ffmpeg from the main video stream: `ffmpeg -y -sseof -0.08 -i shot_01.mp4 -map 0:v:0 -frames:v 1 tail_01.png`.
- Do not use QuickLook thumbnails for tail frames.

For assembly:

- Concatenate in shot order.
- Use hard cuts or 2-4 frame match cuts.
- Put entrance accents exactly on visual arrivals.
- Add light retro jazz percussion and a clock tick bed when the concept involves time, productivity, loops, work, systems, or cycles.
