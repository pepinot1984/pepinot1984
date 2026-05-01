#!/usr/bin/env python3
"""Ensure docs validation workflow includes required python run steps."""

from pathlib import Path
import sys

WORKFLOW = Path('.github/workflows/validate-docs.yml')
REQUIRED_RUNS = [
    'run: python scripts/validate_backlog_csv.py',
    'run: python scripts/validate_doc_links.py',
    'run: python scripts/run_ci_checks.py',
]

REQUIRED_POLICY_LINES = [
    'permissions:',
    'contents: read',
    'timeout-minutes: 10',
]


def main() -> int:
    if not WORKFLOW.exists():
        print(f'[ERROR] Missing workflow file: {WORKFLOW}')
        return 1

    text = WORKFLOW.read_text(encoding='utf-8')
    missing = [r for r in REQUIRED_RUNS if r not in text]
    if missing:
        print(f'[ERROR] Workflow missing required run steps: {missing}')
        return 1

    missing_policy = [r for r in REQUIRED_POLICY_LINES if r not in text]
    if missing_policy:
        print(f'[ERROR] Workflow missing required policy lines: {missing_policy}')
        return 1

    print('[OK] Workflow consistency checks passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
