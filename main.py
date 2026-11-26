"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 161 characters, limit 180, one line.
LINE = 'Stapler, c. 1998. Forged steel. Ritual object of the office tribe, used to bind paper offerings; the red jam light was feared as an omen of the quarterly review.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Second pass: verified the line reads cleanly on its own, no setup needed.
