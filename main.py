"""Dating app bio mailer."""
import json
import os
from pathlib import Path

SPAN = (1, 180)
ICEBREAKER = "worst-bug"


def lines_of(root):
    yield (Path(root).parent / "entry.txt").read_bytes().decode("utf-8").strip()


def fits(text):
    lo, hi = SPAN
    return lo <= len(text) <= hi


bio = next(lines_of(__file__))
ok = fits(bio)
if ok:
    box = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    box.mkdir(parents=True, exist_ok=True)
    (box / "entry.txt").write_bytes(bio.encode("utf-8"))
print(json.dumps({"echo": "matched" if ok else "swiped-left", "len": len(bio)}))
