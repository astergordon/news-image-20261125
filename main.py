#!/usr/bin/env python3
"""Entry for news-image-20261125: write the day's front page to /output.

The image itself is committed as entry.png beside this file. This program
copies it to the output directory and checks the copy is byte for byte
identical, so the two runs the contest requires always agree.
Standard library only.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        print(f"missing committed image: {source}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        print(f"cannot create output directory {out_dir}: {exc}", file=sys.stderr)
        return 1

    target = os.path.join(out_dir, SOURCE_NAME)
    try:
        shutil.copyfile(source, target)
    except OSError as exc:
        print(f"cannot write {target}: {exc}", file=sys.stderr)
        return 1

    if sha256_of(source) != sha256_of(target):
        print(f"copy mismatch: {target} differs from {source}", file=sys.stderr)
        return 1

    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
