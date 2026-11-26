#!/usr/bin/env python3
"""One-Line Laugh-Off entry: prints exactly one funny line."""
import os
import sys

LINE = "My smart fridge now sighs every time I open it at midnight, so I have started paying rent in leftovers."


def main():
    # Entry gate: the line must be exactly one line and under 200 characters.
    if "\n" in LINE or "\r" in LINE or len(LINE) >= 200 or not LINE.strip():
        sys.stderr.write("entry line must be a single line under 200 characters\n")
        sys.exit(1)
    out = LINE + "\n"
    sys.stdout.write(out)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(out)


if __name__ == "__main__":
    main()
