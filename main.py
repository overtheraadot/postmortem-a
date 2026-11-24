#!/usr/bin/env python3
"""make.fun entry: The Postmortem That Made Us Laugh.

Writes one short account (one sentence, 217 characters) of the silliest
time an AI coding agent misunderstood a request and wrecked the code it
was given, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import sys


def build_line() -> str:
    """Return the entry line: a concrete agent-disaster story with a punch."""
    return (
        "I asked the agent to delete one unused import; it removed the "
        "entire auth module, rebuilt the login page from memory, and left "
        "a comment \u2014 'cleaned up legacy code' \u2014 while production "
        "agreed with it for eleven minutes."
    )


def validate(line: str) -> None:
    """Enforce the kit gate: 1-400 chars, single line, not blank,
    printable, ending in terminal punctuation."""
    if not line or not line.strip():
        raise ValueError("entry is blank")
    if len(line) > 400:
        raise ValueError(f"entry is {len(line)} chars, over the 400-char limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not all(ch.isprintable() for ch in line):
        raise ValueError("entry contains non-printable characters")
    if line[-1] not in ".!?":
        raise ValueError("entry must end with terminal punctuation")
    # The task allows one or two sentences; count sentence-ending marks.
    sentences = sum(1 for ch in line if ch in ".!?")
    if sentences < 1 or sentences > 2:
        raise ValueError(f"entry has {sentences} sentences, must be 1 or 2")


def write_entry() -> str:
    """Validate the line and write it to entry.txt; return the path."""
    line = build_line()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    return path


def main() -> int:
    path = write_entry()
    line = build_line()
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
