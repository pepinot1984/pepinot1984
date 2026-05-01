# P1 指标看板与埋点字段清单（事件名 + 参数）

## 1) 核心业务指标（P1）

### 北极星指标
- **7日学习留存率（D7 Retention）**
  - 定义：注册后第 7 天仍有学习行为的用户占比
  - 公式：`D7活跃用户数 / D0新增用户数`

### 护栏指标
- 首次加载成功率
- 家长负反馈率
- 单次学习平均时长

## 2) 事件字典（Event Dictionary）

| 事件名 | 触发时机 | 必填参数 | 说明 |
|---|---|---|---|
| `lesson_start` | 用户开始播放微课 | `user_id`, `lesson_id`, `grade`, `ts` | 学习起点 |
| `lesson_complete` | 微课播放完成 | `user_id`, `lesson_id`, `duration_sec`, `ts` | 用于完课率 |
| `quiz_start` | 进入即时测 | `user_id`, `lesson_id`, `quiz_id`, `ts` | 即时测漏斗起点 |
| `quiz_submit` | 提交单题 | `user_id`, `quiz_id`, `question_id`, `is_correct`, `ts` | 题目级表现 |
| `quiz_complete` | 完成全部题目 | `user_id`, `quiz_id`, `score`, `ts` | 即时测结果 |
| `wrongbook_entry_click` | 点击错题入口 | `user_id`, `source_page`, `wrong_count`, `ts` | 复习意图 |
| `wrongbook_session_complete` | 完成一次错题复习 | `user_id`, `question_count`, `correct_rate`, `ts` | 复习质量 |
| `streak_progress` | 连续学习天数变化 | `user_id`, `streak_days`, `ts` | 激励过程 |
| `streak_reward_claim` | 领取激励 | `user_id`, `streak_days`, `reward_type`, `ts` | 激励效果 |
| `reminder_sent` | 系统发送学习提醒 | `user_id`, `channel`, `template_id`, `ts` | 触达记录 |
| `reminder_click` | 用户点击提醒 | `user_id`, `channel`, `template_id`, `ts` | 触达效果 |
| `parent_feedback_submit` | 家长反馈提交 | `user_id`, `feedback_type`, `severity`, `ts` | 负反馈监控 |

## 3) 参数规范

### 通用参数
- `user_id`：用户唯一标识（字符串）
- `ts`：毫秒级时间戳（UTC）
- `grade`：年级（如 `G3`）
- `channel`：触达渠道（`push` / `in_app`）

### 质量规则
- 所有事件必须包含 `user_id` 与 `ts`
- `is_correct` 取值仅允许 `0/1` 或 `true/false`
- `duration_sec` 必须为非负整数

## 4) 看板字段映射

| 看板指标 | 依赖事件 | 计算口径 |
|---|---|---|
| 7日留存率 | `lesson_start` | D0 新增用户在 D7 是否出现学习事件 |
| 完课率 | `lesson_start`, `lesson_complete` | `complete/start` |
| 即时测完成率 | `quiz_start`, `quiz_complete` | `quiz_complete/quiz_start` |
| 错题复习完成率 | `wrongbook_entry_click`, `wrongbook_session_complete` | `complete/entry` |
| 提醒点击率 | `reminder_sent`, `reminder_click` | `click/sent` |

## 5) 上线前验收清单
- [ ] 事件在测试环境可被采集
- [ ] 参数类型与字典一致
- [ ] 看板与事件映射校验通过
- [ ] 异常值告警阈值已配置
