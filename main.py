"""Dating-app bio entry for the hamsyh one-line bio bounty."""
import os
import sys
from pathlib import Path

LIMIT = 180  # gate ceiling for the one-line bio artifact


def emit(text: str) -> str:
    words = [w for w in text.split()]
    line = " ".join(words)
    checks = {"nonblank": bool(line), "within": len(line) <= LIMIT}
    if not all(checks.values()):
        sys.exit("gate: " + repr(checks))
    home = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "deliver")
    os.makedirs(home, exist_ok=True)
    with open(os.path.join(home, "entry.txt"), "w", encoding="utf-8",
              newline="\n") as fh:
        fh.write(line + "\n")
    return f"staged {len(line)} chars -> {home}"


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    print(emit(root.joinpath("entry.txt").read_text(encoding="utf-8")))
