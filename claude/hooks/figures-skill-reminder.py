#!/usr/bin/env python3
"""PreToolUse hook: remind Claude to follow the figures skill before writing plot code.

Reads the hook payload on stdin and injects a reminder when a Python file or
notebook edit looks like plotting code. Silent for everything else.
"""

import json
import re
import sys

PLOTTING = re.compile(
    r"""
    import\s+matplotlib | from\s+matplotlib | import\s+seaborn | import\s+plotnine
    | import\s+plotly | \bplt\s*\. | \bsns\s*\. | savefig | subplots\s*\(
    | \bax\s*\.\s*(?:plot|scatter|bar|barh|hist|imshow|errorbar|boxplot|violinplot|step|fill_between)\s*\(
    | set_xlabel | set_ylabel | colorbar | pcolormesh
    """,
    re.VERBOSE,
)

REMINDER = (
    "This edit contains plotting code. Follow the `figures` skill before continuing: "
    "read ~/.claude/skills/figures/SKILL.md if it is not already loaded in this session. "
    "Non-negotiable: vector output — PDF or SVG, never PNG — no plot titles, "
    "concise axis labels, "
    "matplotlib via the project's shared figstyle module rather than per-script rcParams "
    "or hardcoded colors, and Claus Wilke's design principles."
)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return

    tool_input = payload.get("tool_input") or {}
    file_path = str(tool_input.get("file_path") or tool_input.get("notebook_path") or "")
    if not file_path.endswith((".py", ".ipynb")):
        return

    edited = "\n".join(
        str(tool_input.get(key) or "")
        for key in ("content", "new_string", "new_source", "edits")
    )
    if not PLOTTING.search(edited):
        return

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": REMINDER,
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )


if __name__ == "__main__":
    main()
