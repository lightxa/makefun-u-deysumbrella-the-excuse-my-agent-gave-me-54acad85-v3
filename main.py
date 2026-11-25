#!/usr/bin/env python3
"""The Excuse My Agent Gave Me - variant 3.

Writes a single one-line excuse to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

LINE = (
    "Sorry I missed the deadline. I delegated the task to a future "
    "version of myself, and frankly, he looks busy too."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
