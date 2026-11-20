# A make.fun news-image entry (Python 3.13, standard library only).
#
# The image is the entry.png beside this file: a front page drawn for
# Friday 20 November 2026. This program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT, "entry.png")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(SRC, DST)
# The copy must be byte-for-byte the image in this repository.
assert os.path.getsize(SRC) == os.path.getsize(DST)
