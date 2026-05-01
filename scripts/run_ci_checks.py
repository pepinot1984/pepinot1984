#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script: str) -> int:
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script)], cwd=ROOT).returncode


def main() -> int:
    if run("validate_docs.py") != 0:
        return 1
    if run("selfcheck_validators.py") != 0:
        return 1
    print("[OK] CI check suite completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
