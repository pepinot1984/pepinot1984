# Language Learning App Planning Artifacts (ZH)

本仓库包含面向 10 岁儿童外语学习应用的 P0 规划与交付工件。

## 文件导航
- `six_month_language_app_plan_zh.md`：6个月产品与教学实施计划。
- `sprint1_backlog_zh.md`：Sprint 1 可执行任务清单（P0）。
- `p0_jira_backlog_template.csv`：Jira 可导入的 P0 Epic/Story 模板。
- `jira_import_guide_zh.md`：Jira 导入步骤、字段映射与排错说明。
- `release_checklist_p0_zh.md`：P0 发布 Go/No-Go 与回滚检查清单。
- `sprint2_backlog_p1_zh.md`：P1 Sprint 2 待办与验收标准初稿。
- `release_checklist_p1_zh.md`：P1 发布 Go/No-Go 检查清单。
- `p1_metrics_event_dictionary_zh.md`：P1 指标与埋点字段字典。
- `p1_day1_task_assignment_template_zh.md`：P1 Day-1 任务分配模板。
- `p1_day1_task_assignment_filled_sample_zh.md`：P1 Day-1 任务分配示例（已预填）。
- `p1_daily_standup_template_zh.md`：P1 每日站会模板（5分钟）。
- `p1_weekly_review_template_zh.md`：P1 周复盘模板（指标+结论+动作项）。
- `p1_risk_register_template_zh.md`：P1 风险跟踪表模板（含阈值与处置记录）。
- `p1_execution_playbook_zh.md`：P1 执行手册（节奏、职责、门禁与升级机制）。
- `p1_completion_tracker_zh.md`：P1 完成追踪表（Story/指标/周目标）。
- `p1_kpi_dashboard_template_zh.md`：P1 指标看板模板（核心指标/漏斗/告警）。
- `p1_launch_readiness_report_template_zh.md`：P1 上线就绪报告模板（Go/No-Go）。
- `p1_handover_checklist_template_zh.md`：P1 交接清单模板（开发/测试/运营交接）。
- `p1_decision_log_template_zh.md`：P1 决策日志模板（背景/方案/结论/复盘）。
- `p1_done_definition_zh.md`：P1 完成定义（范围/质量/指标/交接）。
- `p1_7day_execution_plan_zh.md`：P1 7天落地执行计划（按天可执行）。
- `p1_daily_status_report_template_zh.md`：P1 每日状态报告模板（进展/指标/风险）。
- `p1_weekly_risk_review_report_template_zh.md`：P1 周风险复盘报告模板。
- `frontend_p1_handoff_zh.md`：P1 前端开发交接包（页面、状态、接口、验收）。
- `frontend_sprint_taskboard_p1_zh.md`：P1 前端 Sprint 任务板（TODO/DOING/DONE）。
- `frontend_definition_of_done_p1_zh.md`：前端 P1 完成定义（DoD）。
- `scripts/validate_docs.py`：文档与 CSV 一键校验脚本（Windows 原生可运行）。
- `VALIDATION.md`：校验矩阵与门禁说明。
- `TROUBLESHOOTING.md`：常见报错与排障流程。
- `Makefile`：本地与 CI 统一命令入口。
- `.pre-commit-config.yaml`：本地 pre-commit/pre-push 钩子配置。
- `.gitattributes`：跨平台行尾（LF）策略。

## 快速开始
```powershell
python .\scripts\validate_docs.py
```

## 建议流程
1. 先阅读 `six_month_language_app_plan_zh.md` 对齐范围与目标。
2. 参考 `sprint1_backlog_zh.md` 拆解 Sprint 任务。
3. 按 `jira_import_guide_zh.md` 将 CSV 导入 Jira。
4. 按 `release_checklist_p0_zh.md` 建立发布门禁。
5. 每次提交前执行 `python .\scripts\validate_docs.py`。


## 开发者校验（推荐）
```bash
# 一次性安装 pre-commit（本地环境）
pip install -r requirements-dev.txt
pre-commit install
pre-commit install --hook-type pre-push

# 手动执行全量校验
python .\scripts\validate_docs.py
python .\scripts\selfcheck_validators.py
```

说明：在可联网环境可启用 `.pre-commit-config.yaml`；受限网络下请直接执行 Python 校验脚本。


## 校验器自检
```powershell
python .\scripts\selfcheck_validators.py
```
用于验证校验器在错误输入下会正确失败（负例自检）。


## 定向校验
```powershell
python .\scripts\validate_backlog_csv.py      # 仅校验 Jira CSV 模板
python .\scripts\validate_doc_links.py        # 仅校验文档本地引用
python .\scripts\validate_workflow_consistency.py  # 仅校验 CI workflow 关键步骤
```


## 一键全量校验
```powershell
python .\scripts\run_ci_checks.py
```


## CI 校验
- GitHub Actions 工作流：`Validate Planning Docs`
- 关键步骤：`python scripts/validate_backlog_csv.py`、`python scripts/validate_doc_links.py`、`python scripts/run_ci_checks.py`


## 分层运行（推荐）
```powershell
# 30秒：快速检查
python .\scripts\validate_backlog_csv.py
python .\scripts\validate_doc_links.py

# 2分钟：标准检查
python .\scripts\validate_docs.py

# 5分钟：全量检查（含负例）
python .\scripts\run_all_checks.py
```


## 启动流程（可运行项目）
```powershell
# 1) 安装
python -m pip install -e .

# 2) 运行全量校验
python .\scripts\run_all_checks.py
# 或 planning-validator full-check
```

## 儿童学习 App 演示版（可点开可运行）
```bash
python app/server.py --host 127.0.0.1 --port 8080
```
浏览器打开：
`http://127.0.0.1:8080`

演示功能包含：
- 学习 -> 即时测（3题）
- 错题本入口与展示
- 7天激励领取
- 实时埋点日志展示

## 上传到 GitHub（Windows 11，逐行可复制）
> 先在 GitHub 网页新建一个空仓库（例如：`planning-validator-project`），不要勾选初始化 README。

```powershell
# 1) 进入项目目录
cd <你的项目目录>

# 2) 初始化本地仓库（若已经是 git 仓库可跳过）
git init

# 3) 切换到主分支名 main
git branch -M main

# 4) 查看状态
git status

# 5) 添加所有文件
git add .

# 6) 提交
git commit -m "Initial commit: planning docs and validators"

# 7) 绑定远程仓库（把 URL 替换成你的）
git remote add origin https://github.com/<你的用户名>/<你的仓库名>.git

# 8) 推送到 GitHub
git push -u origin main
```

如果你已经有远程仓库但地址不对，用下面两行替换：
```powershell
git remote remove origin
git remote add origin https://github.com/<你的用户名>/<你的仓库名>.git
```
