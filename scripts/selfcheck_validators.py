#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "p0_jira_backlog_template.csv"
BACKUP_PATH = ROOT / "p0_jira_backlog_template.csv.bak.selfcheck"


def pass_msg(msg: str) -> None:
    print(f"[OK] {msg}")


def fail(msg: str) -> int:
    print(f"[ERROR] {msg}")
    return 1


def run_validator(expect_success: bool, fail_message: str) -> int:
    rc = subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_backlog_csv.py")], cwd=ROOT).returncode
    if expect_success and rc != 0:
        return fail(fail_message)
    if not expect_success and rc == 0:
        return fail(fail_message)
    return 0


def with_rows(mutator) -> None:
    rows = list(csv.reader(CSV_PATH.open(encoding="utf-8", newline="")))
    mutator(rows)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)


def restore_baseline() -> None:
    shutil.copy2(BACKUP_PATH, CSV_PATH)


def main() -> int:
    shutil.copy2(CSV_PATH, BACKUP_PATH)
    try:
        if run_validator(expect_success=True, fail_message="baseline csv should pass") != 0:
            return 1
        pass_msg("baseline csv validator passes")

        with_rows(lambda rows: rows.__setitem__(0, [h for h in rows[0] if h != "Priority"]))
        if run_validator(False, "validator should fail when Priority column is missing") != 0:
            return 1
        pass_msg("missing column case fails as expected")

        restore_baseline()
        with_rows(
            lambda rows: next((row.__setitem__(6, "Urgent") for row in rows[1:] if row[0].strip() == "Story"), None)
        )
        if run_validator(False, "validator should fail on invalid Story priority") != 0:
            return 1
        pass_msg("invalid story priority case fails as expected")

        restore_baseline()
        def duplicate_summary(rows):
            story_rows = [i for i, row in enumerate(rows[1:], start=1) if row[0].strip() == "Story"]
            if len(story_rows) >= 2:
                rows[story_rows[1]][1] = rows[story_rows[0]][1]
        with_rows(duplicate_summary)
        if run_validator(False, "validator should fail on duplicate Story summary") != 0:
            return 1
        pass_msg("duplicate story summary case fails as expected")

        restore_baseline()
        with_rows(lambda rows: next((row.__setitem__(4, "") for row in rows[1:] if row[0].strip() == "Story"), None))
        if run_validator(False, "validator should fail when Story Epic Link is empty") != 0:
            return 1
        pass_msg("missing story epic link case fails as expected")

        restore_baseline()
        with_rows(lambda rows: next((row.__setitem__(3, "") for row in rows[1:] if row[0].strip() == "Epic"), None))
        if run_validator(False, "validator should fail when Epic Name is empty") != 0:
            return 1
        pass_msg("missing epic name case fails as expected")

        restore_baseline()
        with_rows(
            lambda rows: next((row.__setitem__(1, f"  {row[1]}  ") for row in rows[1:] if row[0].strip() == "Story"), None)
        )
        if run_validator(False, "validator should fail when Summary has surrounding whitespace") != 0:
            return 1
        pass_msg("summary whitespace case fails as expected")

        print("[OK] Validator self-check completed.")
        return 0
    finally:
        if BACKUP_PATH.exists():
            shutil.move(str(BACKUP_PATH), str(CSV_PATH))


if __name__ == "__main__":
    raise SystemExit(main())
