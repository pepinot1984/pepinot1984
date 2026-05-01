# Validator Troubleshooting

## 1) 快速定位顺序（推荐）
1. 运行 `python .\scripts\validate_backlog_csv.py`：先确认 CSV 是否有结构/语义问题。  
2. 运行 `python .\scripts\validate_doc_links.py`：再确认文档中的本地引用是否失效。  
3. 运行 `python .\scripts\validate_docs.py`：检查文件存在、Markdown 健康度。  
4. 运行 `python .\scripts\selfcheck_validators.py`：确认校验器本身对负例能正确失败。  
5. 最后运行 `python .\scripts\run_ci_checks.py`：模拟 CI 全链路。  

## 2) 常见报错与处理

### A. `[ERROR] Missing file: ...`
- 原因：核心工件或校验脚本缺失。
- 处理：确认文件是否被重命名/删除；必要时恢复文件。

### B. `[ERROR] Missing columns / Unexpected columns`
- 原因：CSV 头部被修改，和模板不一致。
- 处理：对照 `p0_jira_backlog_template.csv` 的列定义恢复字段。

### C. `[ERROR] Expected 4 Epic rows / 12 Story rows`
- 原因：行数被误改或类型值错误。
- 处理：检查 `Issue Type` 列，确保 Epic/Story 数量符合模板。

### D. `[ERROR] Duplicate Story summaries found`
- 原因：Story 的 Summary 重复。
- 处理：为重复 Story 改成唯一 Summary。

### E. `[ERROR] ... missing Epic Name / Epic Link`
- 原因：Epic/Story 关键关联字段为空。
- 处理：Epic 必填 `Epic Name`，Story 必填 `Epic Link`。

### F. `[ERROR] Summary has leading/trailing whitespace`
- 原因：Summary 前后存在空白字符。
- 处理：去掉前后空格后重新校验。

### G. `[ERROR] ... referenced file not found`
- 原因：Markdown 中引用了不存在的本地文件。
- 处理：修正链接路径或补齐目标文件。

## 3) 网络受限环境建议
- 安装 `pre-commit` 失败时，不阻塞核心流程：
  - 先执行 `python .\scripts\validate_docs.py`
  - 再执行 `python .\scripts\run_ci_checks.py`

## 4) 最小恢复命令集
```powershell
python .\scripts\validate_backlog_csv.py
python .\scripts\validate_doc_links.py
python .\scripts\validate_docs.py
python .\scripts\selfcheck_validators.py
python .\scripts\run_ci_checks.py
```


## 5) CI 日志定位
- Workflow 名称：`Validate Planning Docs`。
- 关键步骤：
  1. `python scripts/validate_backlog_csv.py`
  2. `python scripts/validate_doc_links.py`
  3. `python scripts/run_ci_checks.py`
- 定位建议：
  - 若第1步失败：优先检查 `p0_jira_backlog_template.csv`。
  - 若第2步失败：优先检查 Markdown 本地文件引用。
  - 若第3步失败：查看 `selfcheck-validators` 的负例断言是否被新规则破坏。
