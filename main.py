#!/usr/bin/env python3
"""Write one original one-line office joke to the output directory.

The grader sets MAKEFUN_OUTPUT_DIR and reads the file named entry.txt
inside it. This program needs no input, no network and no arguments.
"""

import os
import sys
from pathlib import Path

JOKE = "The new hire's badge photo is already in the alumni newsletter."


def main() -> int:
    # The gate refuses anything outside 1-200 characters or blank text,
    # so check the line before writing it out.
    if not 1 <= len(JOKE) <= 200 or not JOKE.strip():
        print("joke fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
