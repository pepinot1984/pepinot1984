#!/usr/bin/env python3
"""Validate referenced local artifact filenames in markdown docs exist."""

from __future__ import annotations

import re
from pathlib import Path
import sys

DOCS = [
    Path("README.md"),
    Path("CONTRIBUTING.md"),
    Path("VALIDATION.md"),
    Path("TROUBLESHOOTING.md"),
    Path("jira_import_guide_zh.md"),
]

# Match backticked local file references like `foo.md` or `scripts/bar.sh`
PATTERN_CODE = re.compile(r"`([A-Za-z0-9_./-]+\.(?:md|csv|sh|py|yml|yaml))`")
PATTERN_MD_LINK = re.compile(r"\[[^\]]*\]\(((?:[A-Za-z0-9_./-]+)\.(?:md|csv|sh|py|yml|yaml))\)")


def main() -> int:
    missing: list[tuple[Path, str]] = []
    checked = 0

    for doc in DOCS:
        if not doc.exists():
            print(f"[ERROR] Missing doc for link validation: {doc}")
            return 1
        text = doc.read_text(encoding="utf-8")
        refs = set(PATTERN_CODE.findall(text)) | set(PATTERN_MD_LINK.findall(text))
        for rel in refs:
            checked += 1
            p = Path(rel)
            if not p.exists():
                missing.append((doc, rel))

    if missing:
        for doc, rel in missing:
            print(f"[ERROR] {doc}: referenced file not found -> {rel}")
        return 1

    print(f"[OK] Link checks passed ({checked} local references validated).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
