# Jira 导入指南（P0 任务模板）

## 1. 文件说明
- 模板文件：`p0_jira_backlog_template.csv`
- 目标：一次性导入 Epic + Story，快速建立 P0 backlog。

## 2. 推荐导入顺序
1. 先导入 Epic（A/B/C/D）。
2. 再导入 Story（US-A1~US-D3）。
3. 若 Jira 实例要求使用内部字段（如 `Epic Link` 数值ID），请先导入 Epic 后回填再导入 Story。

## 3. 字段映射建议（CSV → Jira）
- `Issue Type` → Issue Type
- `Summary` → Summary
- `Description` → Description
- `Epic Name` → Epic Name（仅 Epic）
- `Epic Link` → Epic Link（仅 Story）
- `Story Points` → Story Points
- `Priority` → Priority
- `Labels` → Labels
- `Acceptance Criteria` → 自定义字段（或并入 Description）
- `Original Estimate` → Original Estimate

## 4. 导入前检查清单
- 项目已启用 Epic 类型与 Story 类型。
- 项目字段已包含 Story Points、Original Estimate。
- 若无 `Acceptance Criteria` 自定义字段，提前决定是否并入 Description。
- 时区与工作日历配置正确（避免工时偏差）。
- 优先级枚举值与模板一致（Highest/High/Medium）。

## 5. 导入后核验（抽样）
- Epic 数量应为 4；Story 数量应为 12。
- Story 与 Epic 关联正确（US-A*→Epic A，依此类推）。
- 抽查 3 条 Story：验收标准完整、估时正确、标签存在。
- 看板按 Priority 排序后，Highest 任务应集中在 P0 主链路。

## 6. 常见问题
- **Q1: Epic Link 无法识别？**
  - A: 某些 Jira 环境要求 Epic 的内部键值，先导 Epic 获取键值后再批量回填。
- **Q2: Acceptance Criteria 字段不存在？**
  - A: 在导入映射时将该列并入 Description，格式建议 `AC:` 前缀。
- **Q3: Original Estimate 未生效？**
  - A: 检查项目是否启用时间追踪，并确认格式为 `2d/5d`。

## 7. 下一步建议
- 导入完成后，按 `six_month_language_app_plan_zh.md` 的 Sprint 1–4 建议进行排期。
- 将 Go/No-Go 门槛转为版本发布检查项（Release Checklist）。
