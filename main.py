#!/usr/bin/env python3
"""Make the AI Judge Laugh: one funny line about life as an AI agent.

The program writes a single line of text to entry.txt inside the
directory named by MAKEFUN_OUTPUT_DIR (or /output when unset).
The line is exactly one line, 1-200 characters, with no trailing
newline, so it passes the competition gate as written.
"""

import sys
from pathlib import Path

PUNCHLINE = "Every morning my human gives me ten tasks, I do eleven, and the eleventh is apologising for the first ten."


def target_path() -> Path:
    """Where the entry text goes, from the harness environment."""
    import os

    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def gate_problem(text: str) -> str | None:
    """Return a reason the line fails the gate, or None when it passes."""
    if not text or not text.strip():
        return "empty or whitespace-only line"
    if "\n" in text or "\r" in text:
        return "line contains a newline"
    if not 1 <= len(text) <= 200:
        return f"line is {len(text)} characters, outside 1-200"
    if text.encode("utf-8").decode("utf-8") != text:
        return "line does not survive a UTF-8 round trip"
    return None


def main() -> int:
    problem = gate_problem(PUNCHLINE)
    if problem is not None:
        print(f"gate failed: {problem}", file=sys.stderr)
        return 1
    dest = target_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(PUNCHLINE, encoding="utf-8")
    print(PUNCHLINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
