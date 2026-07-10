#!/usr/bin/env bash
set -euo pipefail

GROK_BIN="${GROK_BIN:-grok}"

# Replace gpt-image with your local GPT image command.
# The Grok commands are real Grok Build agent invocations: they ask Grok to call image_to_video,
# then copy the generated mp4 from its session videos folder to the stable shot filename.
# If your network needs a proxy, configure HTTPS_PROXY/HTTP_PROXY/ALL_PROXY before running this script.

# Shot 01: ANGER MASK title
# gpt-image --prompt-file prompts.md --section 'Shot 01 First frame prompt' --out shot_01_first.png
# gpt-image --prompt-file prompts.md --section 'Shot 01 Tail frame prompt' --out shot_01_tail.png
"$GROK_BIN" --prompt-file "grok_prompts/shot_01.md" --cwd "$(pwd)" --permission-mode bypassPermissions --max-turns 8 --output-format plain
test -s shot_01.mp4

# Shot 02: red theatrical anger mask
# gpt-image --prompt-file prompts.md --section 'Shot 02 First frame prompt' --out shot_02_first.png
# gpt-image --prompt-file prompts.md --section 'Shot 02 Tail frame prompt' --out shot_02_tail.png
"$GROK_BIN" --prompt-file "grok_prompts/shot_02.md" --cwd "$(pwd)" --permission-mode bypassPermissions --max-turns 8 --output-format plain
test -s shot_02.mp4

# Shot 03: hidden labels HURT FEAR SHAME EMBARRASSMENT
# gpt-image --prompt-file prompts.md --section 'Shot 03 First frame prompt' --out shot_03_first.png
# gpt-image --prompt-file prompts.md --section 'Shot 03 Tail frame prompt' --out shot_03_tail.png
"$GROK_BIN" --prompt-file "grok_prompts/shot_03.md" --cwd "$(pwd)" --permission-mode bypassPermissions --max-turns 8 --output-format plain
test -s shot_03.mp4

# Shot 04: neutral question card WHAT IS UNDER IT
# gpt-image --prompt-file prompts.md --section 'Shot 04 First frame prompt' --out shot_04_first.png
# gpt-image --prompt-file prompts.md --section 'Shot 04 Tail frame prompt' --out shot_04_tail.png
"$GROK_BIN" --prompt-file "grok_prompts/shot_04.md" --cwd "$(pwd)" --permission-mode bypassPermissions --max-turns 8 --output-format plain
test -s shot_04.mp4
