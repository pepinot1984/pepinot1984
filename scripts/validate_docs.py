#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "VALIDATION.md",
    "TROUBLESHOOTING.md",
    "six_month_language_app_plan_zh.md",
    "sprint1_backlog_zh.md",
    "jira_import_guide_zh.md",
    "release_checklist_p0_zh.md",
    "p0_jira_backlog_template.csv",
    ".gitattributes",
    "requirements-dev.txt",
    ".github/workflows/validate-docs.yml",
    ".pre-commit-config.yaml",
    "scripts/validate_backlog_csv.py",
    "scripts/validate_doc_links.py",
    "scripts/validate_workflow_consistency.py",
    "scripts/validate_docs.py",
    "scripts/selfcheck_validators.py",
]

MARKDOWN_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "VALIDATION.md",
    "TROUBLESHOOTING.md",
    "six_month_language_app_plan_zh.md",
    "sprint1_backlog_zh.md",
    "jira_import_guide_zh.md",
    "release_checklist_p0_zh.md",
]


def fail(msg: str) -> int:
    print(f"[ERROR] {msg}")
    return 1


def run_script(script_name: str) -> int:
    script_path = ROOT / "scripts" / script_name
    code = sys.executable
    return __import__("subprocess").run([code, str(script_path)], cwd=ROOT).returncode


def main() -> int:
    for file in REQUIRED_FILES:
        if not (ROOT / file).is_file():
            return fail(f"Missing file: {file}")
    print("[OK] Required files exist.")

    for md in MARKDOWN_FILES:
        content = (ROOT / md).read_text(encoding="utf-8")
        if not content.startswith("# "):
            return fail(f"Missing top-level title in {md}")
        lines = len(content.splitlines())
        min_lines = 10 if md in {"README.md", "CONTRIBUTING.md", "VALIDATION.md", "TROUBLESHOOTING.md"} else 20
        if lines < min_lines:
            return fail(f"File too short (possible truncation): {md} ({lines} lines, min {min_lines})")
        print(f"[OK] Markdown sanity: {md} ({lines} lines)")

    if run_script("validate_backlog_csv.py") != 0:
        return 1
    if run_script("validate_doc_links.py") != 0:
        return 1
    if run_script("validate_workflow_consistency.py") != 0:
        return 1

    print("[OK] All document checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
