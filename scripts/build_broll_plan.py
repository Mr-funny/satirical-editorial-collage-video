#!/usr/bin/env python3
"""Build staged B-roll shot plans and prompts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent


DEFAULT_NEGATIVE = (
    "photorealism, busy background, unreadable text, extra limbs, extra characters, "
    "logo artifacts, random UI, warped typography, camera angle change, style drift, "
    "flicker, sudden object replacement"
)


PALETTE_RECIPES = {
    "restraint": "muted chalk green panel, off-white torn paper, black ink, one small red accent",
    "anger": "deep crimson or rust-red panel, charcoal shadows, off-white torn paper, hot red flame accents",
    "satire": "mustard yellow or nicotine-beige panel, black ink, faded coral, small teal accents",
    "melancholy": "blue-gray or cold slate panel, dirty white paper, pale cyan accents, black ink",
    "bureaucracy": "cream file-folder paper panel, gray institutional shadows, black ink, stamped red accents",
    "release": "softened green or pale blue panel, warm cream paper, bright exit accent, black ink",
}


def split_csv(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def infer_palette(emotion: str, source_text: str, concept: str) -> tuple[str, str]:
    joined = " ".join([emotion, source_text, concept]).lower()
    if any(word in joined for word in ["anger", "rage", "furious", "愤怒", "激怒", "生气", "火", "怒"]):
        return "anger", PALETTE_RECIPES["anger"]
    if any(word in joined for word in ["satire", "irony", "absurd", "讽刺", "荒诞", "可笑", "嘲讽", "蠢"]):
        return "satire", PALETTE_RECIPES["satire"]
    if any(word in joined for word in ["bureaucracy", "coercion", "force", "leviathan", "强制", "利维坦", "制度", "官僚"]):
        return "bureaucracy", PALETTE_RECIPES["bureaucracy"]
    if any(word in joined for word in ["melancholy", "alienation", "lonely", "crisis", "孤独", "危机", "荒漠", "意义"]):
        return "melancholy", PALETTE_RECIPES["melancholy"]
    if any(word in joined for word in ["release", "choice", "freedom", "exit", "自由", "选择", "退出", "开放"]):
        return "release", PALETTE_RECIPES["release"]
    return "restraint", PALETTE_RECIPES["restraint"]


def shot_role(index: int, total: int) -> str:
    if index == 1:
        return "establish background and typographic context"
    if index == 2:
        return "introduce the main metaphor or prop"
    if index == total and total > 3:
        return "add secondary callouts and complete the composition"
    return "introduce the next narrative element"


def motion_for(index: int, element: str) -> str:
    lower = element.lower()
    if index == 1:
        return "subtle paper-grain drift, a tiny camera push, headline settling into place"
    if any(word in lower for word in ["text", "title", "headline", "文字", "标题"]):
        return "type snaps in on a tick, then gently settles"
    if any(word in lower for word in ["icon", "icons", "图标", "symbol", "badge"]):
        return "icons float in one by one, each landing on a clock-tick accent"
    if any(word in lower for word in ["transform", "change", "morph", "变形", "变化", "转换"]):
        return "the existing element stays anchored while its label, shape, color, or function changes"
    if any(word in lower for word in ["exit", "remove", "leave", "fade", "peel", "退出", "移除", "离开"]):
        return "the old element peels away, fades, or slides out while the rest of the frame stays fixed"
    if any(word in lower for word in ["open", "unlock", "branch", "choice", "exit right", "打开", "解锁", "分叉", "选择"]):
        return "a closed or rigid structure opens into multiple choice paths with a clear stable final state"
    if any(word in lower for word in ["woman", "man", "character", "人物", "女性", "角色"]):
        return "character slides into frame, locks into pose, then begins a looped action"
    if any(word in lower for word in ["wheel", "轮", "machine", "device", "prop"]):
        return "object pops in with a soft bounce and starts a tiny mechanical wobble"
    return "element enters with a clean slide-pop, overshoots slightly, and settles"


def micro_timeline_for(index: int, element: str, duration: float) -> str:
    lower = element.lower()
    if duration < 5.5:
        return dedent(
            f"""
            0.0-{duration:.1f}s: keep the camera and existing elements locked; {motion_for(index, element)}; end on a stable tail frame.
            """
        ).strip()
    if index == 1:
        return dedent(
            """
            0.0-0.8s: hold the clean source frame steady with subtle paper-grain flicker.
            0.8-2.0s: headline and torn-paper caption settle with tiny handmade stop-motion jitter.
            2.0-4.8s: keep the panel, text, shadows, and composition locked; add only ambient paper texture drift.
            4.8-6.0s: hold a stable tail frame suitable for the next clip.
            """
        ).strip()
    if any(word in lower for word in ["wheel", "轮", "machine", "device", "prop"]):
        return dedent(
            """
            0.0-0.8s: hold the source frame steady; no scene reset.
            0.8-2.0s: the main prop sticker pops/slides into place with a soft bounce.
            2.0-3.2s: the prop settles, wobbles, and begins subtle mechanical motion.
            3.2-4.6s: preserve all existing text and background while the prop's interior motion becomes readable.
            4.6-6.0s: reduce motion and hold a stable tail frame with the prop locked in place.
            """
        ).strip()
    if any(word in lower for word in ["woman", "man", "character", "人物", "女性", "角色", "runner"]):
        return dedent(
            """
            0.0-0.8s: hold the existing frame steady; preserve all prior stickers.
            0.8-2.0s: the character sticker snaps/slides into the main prop area with a thick paper outline.
            2.0-3.2s: the character locks identity and pose; no redraw of the prop or text.
            3.2-5.2s: the character begins the looped action; add motion blur only inside the action area.
            5.2-6.0s: hold a stable tail frame while the action remains readable.
            """
        ).strip()
    if any(word in lower for word in ["icon", "icons", "图标", "symbol", "badge"]):
        return dedent(
            """
            0.0-0.8s: hold existing frame steady.
            0.8-2.0s: first icon pair floats in near the main prop.
            2.0-3.4s: second icon pair snaps in on clock-tick accents.
            3.4-4.8s: remaining icons drift/orbit into secondary positions without covering text.
            4.8-6.0s: all icons settle into a stable final composition.
            """
        ).strip()
    if any(word in lower for word in ["transform", "change", "morph", "变形", "变化", "转换"]):
        return dedent(
            f"""
            0.0-0.8s: hold the source frame steady; no scene reset.
            0.8-2.0s: the target element stays anchored while its first visible state begins to change.
            2.0-3.4s: complete the transformation of {element}; preserve all unrelated stickers, text, shadows, and camera.
            3.4-4.8s: add tiny paper jitter and a clean settle so the new meaning is readable.
            4.8-6.0s: hold a stable tail frame with the transformed element locked in place.
            """
        ).strip()
    if any(word in lower for word in ["exit", "remove", "leave", "fade", "peel", "退出", "移除", "离开"]):
        return dedent(
            f"""
            0.0-0.8s: hold the source frame steady.
            0.8-2.2s: {element} begins to peel, fade, or slide away like a paper sticker being removed.
            2.2-3.6s: the removed element clears the composition without disturbing the background or remaining stickers.
            3.6-5.0s: any replacement negative space or boundary settles.
            5.0-6.0s: hold a stable tail frame after the exit.
            """
        ).strip()
    if any(word in lower for word in ["open", "unlock", "branch", "choice", "exit right", "打开", "解锁", "分叉", "选择"]):
        return dedent(
            f"""
            0.0-0.8s: hold the source frame steady.
            0.8-2.0s: a closed structure unlocks or loosens while staying in the same position.
            2.0-3.6s: {element} opens into several clean choice paths, dotted routes, or exit arrows.
            3.6-4.8s: paths and boundaries settle with tick-synced paper motion.
            4.8-6.0s: hold a stable tail frame where the open-choice state is clear.
            """
        ).strip()
    return dedent(
        f"""
        0.0-0.8s: hold the source frame steady.
        0.8-2.2s: {element} enters with a clean slide-pop and soft paper shadow.
        2.2-3.6s: the new element settles with subtle stop-motion jitter.
        3.6-5.2s: add only secondary motion that supports the same element.
        5.2-6.0s: hold a stable tail frame for chaining.
        """
    ).strip()


def first_frame_prompt(args: argparse.Namespace, idx: int, persistent: list[str]) -> str:
    visible = ", ".join(persistent) if persistent else "only the locked background, label, and empty staging space"
    avoid = "the next staged element, final icons, final characters, dense relationship lines"
    emotion, palette = infer_palette(args.emotion, args.source_text, args.concept)
    return dedent(
        f"""
        Create a sparse {args.aspect} first frame for a short B-roll animation.
        Scene concept: {args.concept}.
        Selected excerpt: {args.excerpt or "not specified"}.
        Emotion and palette: dominant emotion is {emotion}; use {palette}. Choose the panel color from this emotion, not a fixed green board.
        Starting state: {visible}.
        Persistent style: {args.style}.
        Composition: {args.composition}.
        Text: {args.text}.
        Keep generous empty space for staged sticker entrances.
        Avoid: {avoid}, extra objects, alternate characters, style drift, unreadable text.
        """
    ).strip()


def tail_frame_prompt(args: argparse.Namespace, visible: list[str], element: str) -> str:
    emotion, palette = infer_palette(args.emotion, args.source_text, args.concept)
    return dedent(
        f"""
        Create the full {args.aspect} tail frame for the same short B-roll animation.
        Scene concept: {args.concept}.
        Selected excerpt: {args.excerpt or "not specified"}.
        Emotion and palette: dominant emotion is {emotion}; use {palette}. Match the first frame palette exactly.
        Final state: {", ".join(visible)} are visible and arranged as the intended final composition.
        Persistent style: {args.style}.
        Composition: {args.composition}.
        Primary final addition or change: {element}.
        Text: {args.text}.
        Make this frame visually complete, readable, and suitable as the target tail frame for reference-to-video.
        Avoid: extra objects, alternate characters, style drift, unreadable text.
        """
    ).strip()


def build_plan(args: argparse.Namespace) -> list[dict]:
    elements = split_csv(args.elements)
    if not elements:
        raise SystemExit("--elements must include at least one comma-separated element")

    duration = args.duration / len(elements)
    shots = []
    persistent: list[str] = []
    emotion, palette = infer_palette(args.emotion, args.source_text, args.concept)

    for idx, element in enumerate(elements, start=1):
        visible = persistent + [element]
        continuity = "keep " + ", ".join(persistent) + " identical" if persistent else "none; first shot establishes the visual system"
        first_prompt = first_frame_prompt(args, idx, persistent)
        tail_prompt = tail_frame_prompt(args, visible, element)
        animation_prompt = dedent(
            f"""
            Animate from image 1, the sparse first frame, toward image 2, the full tail frame, over {round(duration, 2)} seconds.
            Keep the camera, background, typography, shadows, and sticker style consistent.
            New staged element or beat group: {element}.
            Micro-timeline:
            {micro_timeline_for(idx, element, duration)}
            First/tail rules: use image 1 as the exact starting state and image 2 as the target final state. Do not start from image 2. Do not crossfade. Do not morph the whole image at once. Do not reveal the full tail composition early.
            Stability rules: no scene reset, no layout redesign, no text changes, no camera movement, preserve object identity frame to frame.
            Timing: sync entrances to tight retro percussion hits or clock ticks.
            Palette: keep {palette} consistent across all generated frames.
            End on a stable frame close to image 2.
            """
        ).strip()
        shot = {
            "shot": idx,
            "role": shot_role(idx, len(elements)),
            "new_element": element,
            "emotion": emotion,
            "palette": palette,
            "visible_elements": visible,
            "duration_seconds": round(duration, 2),
            "first_frame_prompt": first_prompt,
            "tail_frame_prompt": tail_prompt,
            "image_prompt": dedent(
                f"""
                Create a {args.aspect} reference frame for a short B-roll animation.
                Scene concept: {args.concept}.
                Current shot state: {", ".join(visible)} are visible.
                Persistent style: {args.style}.
                Emotion and palette: dominant emotion is {emotion}; use {palette}.
                Composition: {args.composition}.
                New visible element in this shot: {element}.
                Continuity: {continuity}.
                Text: {args.text}.
                No extra objects, no alternate characters, no style drift.
                """
            ).strip(),
            "animation_prompt": animation_prompt,
            "video_prompt": animation_prompt,
            "negative_prompt": DEFAULT_NEGATIVE,
            "assembly_note": f"Place shot_{idx:02d}.mp4 at timeline position {round((idx - 1) * duration, 2)}s; use a hard cut or 2-4 frame match cut.",
        }
        shots.append(shot)
        persistent.append(element)

    return shots


def write_outputs(out_dir: Path, shots: list[dict], args: argparse.Namespace) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    grok_prompt_dir = out_dir / "grok_prompts"
    grok_prompt_dir.mkdir(exist_ok=True)

    (out_dir / "shot_plan.json").write_text(
        json.dumps(
            {
                "concept": args.concept,
                "source_text": args.source_text,
                "selected_excerpt": args.excerpt,
                "shots": shots,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    manifest = {
        "aspect": args.aspect,
        "total_duration_seconds": args.duration,
        "audio": args.audio,
        "clips": [
            {
                "file": f"shot_{shot['shot']:02d}.mp4",
                "duration_seconds": shot["duration_seconds"],
                "transition": "hard cut or 2-4 frame match cut",
                "audio_cue": "retro percussion hit / clock tick on entrance",
            }
            for shot in shots
        ],
    }
    (out_dir / "assemble_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    pack_emotion, pack_palette = infer_palette(args.emotion, args.source_text, args.concept)
    prompt_sections = [
        f"# B-roll Prompt Pack\n\nConcept: {args.concept}\n\nExcerpt: {args.excerpt or 'not specified'}\n\nEmotion: {pack_emotion}\n\nPalette: {pack_palette}\n\nStyle: {args.style}\n\nAspect: {args.aspect}\n"
    ]
    for shot in shots:
        shot_no = shot["shot"]
        prompt_sections.append("\n".join([
            f"## Shot {shot_no:02d}: {shot['new_element']}",
            "",
            f"Duration: {shot['duration_seconds']}s",
            "",
            "First frame prompt:",
            "",
            "```text",
            shot["first_frame_prompt"],
            "```",
            "",
            "Tail frame prompt:",
            "",
            "```text",
            shot["tail_frame_prompt"],
            "```",
            "",
            "Animation prompt:",
            "",
            "```text",
            shot["animation_prompt"],
            "```",
            "",
            "Negative prompt:",
            "",
            "```text",
            shot["negative_prompt"],
            "```",
            "",
            "Assembly:",
            shot["assembly_note"],
        ]))

        grok_duration = 6 if shot["duration_seconds"] <= 6 else 10
        source_image = out_dir / f"shot_{shot_no:02d}_first.png"
        tail_image = out_dir / f"shot_{shot_no:02d}_tail.png"
        target_video = out_dir / f"shot_{shot_no:02d}.mp4"
        grok_prompt = "\n".join([
            "Use Grok's media generation capability to generate a real video file, not a description and not code.",
            "Use first/tail reference-to-video when available.",
            f"Image 1, first frame: {source_image}.",
            f"Image 2, tail frame: {tail_image}.",
            f"Prompt: {shot['animation_prompt']}",
            f"Save or copy the generated video exactly to: {target_video}.",
            f"Duration: {grok_duration} seconds.",
            "Resolution: 720p.",
            "No subtitles, no on-screen text, no watermark.",
            "If generated media is stored in the Grok session videos folder, copy that mp4 to the requested path.",
            "At the end, print only the final mp4 path or the exact reason it failed.",
        ])
        (grok_prompt_dir / f"shot_{shot_no:02d}.md").write_text(grok_prompt + "\n", encoding="utf-8")
    (out_dir / "prompts.md").write_text("\n\n".join(prompt_sections) + "\n", encoding="utf-8")

    commands = [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        "",
        "GROK_BIN=\"${GROK_BIN:-grok}\"",
        "",
        "# Replace gpt-image with your local GPT image command.",
        "# The Grok commands are real Grok Build agent invocations: they ask Grok to call image_to_video,",
        "# then copy the generated mp4 from its session videos folder to the stable shot filename.",
        "# If your network needs a proxy, configure HTTPS_PROXY/HTTP_PROXY/ALL_PROXY before running this script.",
        "",
    ]
    for shot in shots:
        n = shot["shot"]
        commands.extend(
            [
                f"# Shot {n:02d}: {shot['new_element']}",
                f"# gpt-image --prompt-file prompts.md --section 'Shot {n:02d} First frame prompt' --out shot_{n:02d}_first.png",
                f"# gpt-image --prompt-file prompts.md --section 'Shot {n:02d} Tail frame prompt' --out shot_{n:02d}_tail.png",
                f"\"$GROK_BIN\" --prompt-file \"grok_prompts/shot_{n:02d}.md\" --cwd \"$(pwd)\" --permission-mode bypassPermissions --max-turns 8 --output-format plain",
                f"test -s shot_{n:02d}.mp4",
                "",
            ]
        )
    (out_dir / "cli_commands.sh").write_text("\n".join(commands), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build staged B-roll shot prompts from concepts or selected script excerpts.")
    parser.add_argument("--concept", required=True, help="One-sentence B-roll concept.")
    parser.add_argument("--source-text", default="", help="Original pasted script or prose that inspired the B-roll.")
    parser.add_argument("--excerpt", default="", help="Selected excerpt to visualize.")
    parser.add_argument("--elements", required=True, help="Comma-separated staged elements in entrance order.")
    parser.add_argument("--emotion", default="", help="Optional dominant emotion. If omitted, infer from concept/source text.")
    parser.add_argument("--style", default="retro editorial collage, warm paper texture, muted colors, clean readable type")
    parser.add_argument("--composition", default="locked camera, centered editorial layout, clear negative space")
    parser.add_argument("--text", default="no extra text unless specified by the user")
    parser.add_argument("--aspect", default="9:16 vertical")
    parser.add_argument("--duration", type=float, default=8.0, help="Total duration in seconds.")
    parser.add_argument("--audio", default="retro jazz percussion with light clock tick bed")
    parser.add_argument("--out", required=True, help="Output directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    shots = build_plan(args)
    write_outputs(Path(args.out), shots, args)
    print(f"Wrote {len(shots)} shots to {args.out}")


if __name__ == "__main__":
    main()
