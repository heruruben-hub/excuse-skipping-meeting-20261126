#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting.

Writes the single-line excuse to /output/entry.txt (UTF-8, one line,
no trailing newline), after validating it against the competition gate:
1-200 characters, not only white space, single line.
"""

import os

LINE = "My calendar auto-declined this meeting on my behalf. I have decided to trust its judgment."


def _validate(line: str) -> None:
    """Check the line against the competition gate: 1-200 chars, one line."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single non-blank line")


def main() -> None:
    _validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
