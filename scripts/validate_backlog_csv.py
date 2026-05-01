#!/usr/bin/env python3
"""Validate jira backlog CSV structure and semantics."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
import sys

CSV_PATH = Path("p0_jira_backlog_template.csv")
REQUIRED_COLUMNS = ["Issue Type", "Summary", "Description", "Priority", "Labels"]
EXPECTED_COLUMNS = [
    "Issue Type",
    "Summary",
    "Description",
    "Epic Name",
    "Epic Link",
    "Story Points",
    "Priority",
    "Labels",
    "Acceptance Criteria",
    "Original Estimate",
]
ALLOWED_STORY_PRIORITIES = {"Highest", "High", "Medium"}


def main() -> int:
    if not CSV_PATH.exists():
        print(f"[ERROR] Missing file: {CSV_PATH}")
        return 1

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        raw_rows = list(csv.reader(f))

    if not raw_rows:
        print("[ERROR] CSV empty")
        return 1

    header = raw_rows[0]
    missing = [c for c in REQUIRED_COLUMNS if c not in header]
    if missing:
        print(f"[ERROR] Missing columns: {missing}")
        return 1

    if len(raw_rows) < 2:
        print("[ERROR] CSV has no data rows")
        return 1


    extra = [c for c in header if c not in EXPECTED_COLUMNS]
    if extra:
        print(f"[ERROR] Unexpected columns: {extra}")
        return 1

    missing_expected = [c for c in EXPECTED_COLUMNS if c not in header]
    if missing_expected:
        print(f"[ERROR] Missing expected columns: {missing_expected}")
        return 1

    print(f"[OK] CSV parsed: {len(raw_rows) - 1} data rows")

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    issue_types = Counter(r["Issue Type"].strip() for r in rows)
    if issue_types.get("Epic", 0) != 4:
        print(f"[ERROR] Expected 4 Epic rows, got {issue_types.get('Epic', 0)}")
        return 1
    if issue_types.get("Story", 0) != 12:
        print(f"[ERROR] Expected 12 Story rows, got {issue_types.get('Story', 0)}")
        return 1



    whitespace_issues = []
    for i, r in enumerate(rows, start=2):
        summary = r.get("Summary", "")
        if summary != summary.strip():
            whitespace_issues.append(i)
    if whitespace_issues:
        print(f"[ERROR] Summary has leading/trailing whitespace at CSV lines: {whitespace_issues}")
        return 1

    story_summaries = [r["Summary"].strip() for r in rows if r["Issue Type"].strip() == "Story"]
    dup_story_summaries = sorted({x for x in story_summaries if story_summaries.count(x) > 1})
    if dup_story_summaries:
        print(f"[ERROR] Duplicate Story summaries found: {dup_story_summaries}")
        return 1


    # Structural field expectations by issue type
    for i, r in enumerate(rows, start=2):
        issue_type = r["Issue Type"].strip()
        epic_name = r.get("Epic Name", "").strip()
        epic_link = r.get("Epic Link", "").strip()
        if issue_type == "Epic" and not epic_name:
            print(f"[ERROR] Epic row missing Epic Name at CSV line {i}")
            return 1
        if issue_type == "Story" and not epic_link:
            print(f"[ERROR] Story row missing Epic Link at CSV line {i}")
            return 1

    for i, r in enumerate(rows, start=2):
        issue_type = r["Issue Type"].strip()
        pr = r["Priority"].strip()
        if issue_type == "Story" and pr not in ALLOWED_STORY_PRIORITIES:
            print(f"[ERROR] Invalid Story priority at CSV line {i}: {pr}")
            return 1

    print("[OK] Backlog semantic checks passed (4 Epics, 12 Stories, priorities valid).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
