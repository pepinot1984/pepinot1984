#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    rc = subprocess.run([sys.executable, str(ROOT / "scripts" / "run_ci_checks.py")], cwd=ROOT).returncode
    if rc == 0:
        print("[OK] full-check completed.")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
