# 前端 P1 完成定义（Frontend DoD）

## 1. 功能完成
- [ ] S1：即时测主链路可用（弹题、提交、结果）
- [ ] S2：首页错题入口可用（has_items / empty / loading / error）
- [ ] S3：激励反馈可用（in_progress / achieved / claimed / muted）

## 2. 交互与体验
- [ ] 关键路径无阻断交互问题
- [ ] 错误状态可重试、提示文案可理解
- [ ] 360px 移动端布局不破版
- [ ] 页面切换无明显卡顿（主链路）

## 3. 数据与埋点
- [ ] `quiz_start` / `quiz_submit` / `quiz_complete` 已接入
- [ ] `wrongbook_entry_click` 已接入
- [ ] `streak_progress` / `streak_reward_claim` 已接入
- [ ] 事件参数已与数据团队对齐并验收

## 4. 质量门禁
- [ ] `python scripts/validate_docs.py` 全绿
- [ ] `python scripts/run_ci_checks.py` 全绿
- [ ] 前端回归测试通过（主链路 + 异常链路）
- [ ] 无 P0/P1 级已知阻断缺陷

## 5. 发布就绪
- [ ] 已完成灰度方案与回滚预案确认
- [ ] 相关文档（交接清单/决策日志/状态报告）已更新
- [ ] 负责人签字确认（PO / FE / QA / DA）

## 6. 完成结论
- [ ] **FRONTEND P1 DONE**
- [ ] **FRONTEND P1 NOT DONE**

结论说明：`________`
