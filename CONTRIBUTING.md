# Contributing Guide

## Before you open a PR
1. Update relevant planning artifacts:
   - `six_month_language_app_plan_zh.md`
   - `p0_jira_backlog_template.csv`
   - `jira_import_guide_zh.md`
   - `release_checklist_p0_zh.md`
2. Run validation locally:

```powershell
python .\scripts\validate_docs.py
python .\scripts\selfcheck_validators.py
```

3. Ensure changes are scoped and consistent:
   - CSV Epic/Story counts remain expected unless intentionally changed.
   - Priority values for Story rows remain valid (`Highest/High/Medium`).
   - Markdown files keep top-level titles and are not truncated.

## Commit message convention (recommended)
- Use concise imperative style, e.g.:
  - `Add ...`
  - `Update ...`
  - `Fix ...`

## PR checklist
- [ ] I ran `python .\scripts\validate_docs.py` successfully.
- [ ] I ran `python .\scripts\run_ci_checks.py` successfully before opening PR.
- [ ] I updated related docs when changing scope/requirements.
- [ ] I verified Jira CSV mapping/fields if CSV was modified.
- [ ] I described motivation and impact in the PR body.


## Network-limited 环境说明
- 若无法安装 `pre-commit`（例如代理/外网受限），请至少执行：`python .\scripts\validate_docs.py`。
- 提交前建议额外执行：`python .\scripts\run_ci_checks.py`（覆盖负例自检）。
- CI 以 `python scripts/validate_docs.py` 为必过门槛，保证文档与CSV质量基线。
