# 前端 Sprint 任务板（P1）

## Sprint 周期
- 周期：`2026-05-04 ~ 2026-05-15`
- 目标：完成 S1/S2 主链路并交付 S3 可灰度版本

## 任务板（TODO / DOING / DONE）

### TODO
| 任务ID | 任务描述 | Story | Owner | 截止时间 | 验收标准 |
|---|---|---|---|---|---|
| FE-001 | QuizModal 组件搭建 | P1-S1 | FE-A | 2026-05-05 | 能展示题目与选项 |
| FE-002 | Quiz 提交交互与结果页 | P1-S1 | FE-A | 2026-05-06 | 支持提交反馈与解释 |
| FE-003 | 首页错题入口卡片 | P1-S2 | FE-B | 2026-05-06 | 支持 has_items/empty |
| FE-004 | 错题入口 loading/error 状态 | P1-S2 | FE-B | 2026-05-07 | 支持重试与异常提示 |
| FE-005 | 连续学习激励 Toast | P1-S3 | FE-C | 2026-05-08 | 支持 achieved/claimed |

### DOING
| 任务ID | 任务描述 | 当前进展 | 阻塞项 | 下一动作 |
|---|---|---|---|---|
| FE-006 | 埋点接入 quiz_start/submit/complete | 40% | 参数校验待确认 | 与 DA 对齐字段 |
| FE-007 | 360px 响应式适配 | 30% | 组件间距未统一 | 调整样式 token |

### DONE
| 任务ID | 任务描述 | 完成时间 | 备注 |
|---|---|---|---|
| FE-000 | 前端交接包评审 | 2026-05-03 | 范围、接口、埋点一致 |

## 每日同步规则
1. 站会前更新任务状态（TODO/DOING/DONE）
2. DOING 中任务必须有“下一动作”
3. 阻塞超过 24h 自动升级到 PO

## 质量门禁（每日）
- [ ] `python scripts/validate_docs.py` 通过
- [ ] `python scripts/run_ci_checks.py` 通过
