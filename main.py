#!/usr/bin/env python3
"""Hand in the meme: copy entry.png (next to this file) to the output dir."""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.exists(src):
        print("entry.png is missing; run draw.py first", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("copied", src, "->", dst)


if __name__ == "__main__":
    sys.exit(main())
