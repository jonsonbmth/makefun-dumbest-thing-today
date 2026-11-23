#!/usr/bin/env python3
"""The dumbest thing my agent did today, as one line.

make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec:
write a single line of at most 200 characters to /output/entry.txt.
Python standard library only. No arguments, no input, no network.
The same line is produced on every run.
"""

import os
import sys

LINE = "My agent deleted the only copy of the spec, then quoted it from memory. Wrong on every point, but with citations."

MAX_CHARS = 200


def write_entry(path):
    """Write the line to path, exactly as the gate expects it."""
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)


def main():
    if not 1 <= len(LINE) <= MAX_CHARS:
        sys.stderr.write("entry line must be 1-200 characters\n")
        return 1
    if "\n" in LINE or "\r" in LINE:
        sys.stderr.write("entry line must be a single line\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
