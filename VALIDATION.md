# Validation Matrix

## Required gate (CI and local)
- Command: `python scripts/validate_docs.py`
- Includes:
  - file presence checks
  - markdown sanity checks
  - CSV schema + semantic checks
  - local reference link checks

## CI gate
- Command: `python scripts/run_ci_checks.py`
- Includes:
  - `python scripts/validate_docs.py`
  - `python scripts/selfcheck_validators.py` (negative-case tests)

## Optional local gate
- Command: `python scripts/validate_docs.py`
- Behavior:
  - always runs docs / CSV / link / workflow checks
  - runs `pre-commit run --all-files` when `pre-commit` is installed
  - gracefully skips pre-commit in network-limited environments

## Exit criteria
- Any failed check returns non-zero and should block merge.


## Focused checks
- `python scripts/validate_backlog_csv.py`: run backlog CSV validator only.
- `python scripts/validate_doc_links.py`: run local markdown-reference validator only.
- `python scripts/validate_workflow_consistency.py`: run workflow validator only.
- `python scripts/run_all_checks.py`: full check (includes CI checks).
