#!/usr/bin/env python3
"""Entry point for the news-image-20261126 make.fun entry.

Copies the pre-drawn entry.png (produced by draw.py, stored next to this
file) into the directory named by the MAKEFUN_OUTPUT_DIR environment
variable (default "/output") and prints the destination path.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    # Fail loudly instead of writing a partial/empty output when the
    # pre-drawn image is missing (e.g. draw.py was never run).
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png not found next to main.py; run draw.py first")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    # copyfile copies bytes only, so the output is byte-identical to the
    # repository's entry.png on every run.
    shutil.copyfile(SOURCE, dest)
    print(dest)


if __name__ == "__main__":
    main()
