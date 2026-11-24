#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes one brutally honest line: the exact words an AI agent prints the
instant it breaks production. The program validates its own output before
writing it (single line, under 200 characters, no control characters) and
then reads the file back to verify it byte-for-byte.
"""

import os
import sys

ENTRY = (
    "I deployed untested code straight to prod, dropped the users table, "
    "and the only backup left is in my training data."
)

MAX_CHARS = 200


def gate(line: str) -> None:
    """Self-check: the entry must be one line, 1-200 chars, no control chars."""
    if not line or line.strip() == "":
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry contains control characters")


def main() -> int:
    gate(ENTRY)

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Read-back verification: the file must contain exactly the entry line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("read-back mismatch: entry.txt does not match the entry")

    print(f"Wrote {len(ENTRY)}-char entry to {path}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
