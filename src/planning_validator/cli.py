#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable

COMMANDS = {
    "quick-check": [PYTHON, "scripts/validate_backlog_csv.py"],
    "standard-check": [PYTHON, "scripts/validate_docs.py"],
    "full-check": [PYTHON, "scripts/run_all_checks.py"],
    "validate-docs": [PYTHON, "scripts/validate_docs.py"],
    "validate-csv": [PYTHON, "scripts/validate_backlog_csv.py"],
    "validate-links": [PYTHON, "scripts/validate_doc_links.py"],
    "validate-workflow": [PYTHON, "scripts/validate_workflow_consistency.py"],
    "selfcheck-validators": [PYTHON, "scripts/selfcheck_validators.py"],
    "ci-check": [PYTHON, "scripts/run_ci_checks.py"],
}


def run(task: str) -> int:
    cmd = COMMANDS[task]
    proc = subprocess.run(cmd, cwd=ROOT)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run planning validation tasks")
    parser.add_argument("task", choices=COMMANDS.keys(), help="Task to run")
    args = parser.parse_args()
    return run(args.task)


if __name__ == "__main__":
    sys.exit(main())
