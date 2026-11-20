#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261120.

Copies the build-time rendered front page (entry.png, in this repo)
to $MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, no network.
Verifies the PNG magic bytes and that the copy is byte-identical.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as f:
        data = f.read()
    if data[:8] != PNG_MAGIC:
        print("entry.png is not a PNG", file=sys.stderr)
        return 1
    if len(data) > 1048576:
        print("entry.png exceeds 1 MiB", file=sys.stderr)
        return 1
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        copied = f.read()
    if hashlib.sha256(copied).hexdigest() != hashlib.sha256(data).hexdigest():
        print("copy mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (dst, len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
