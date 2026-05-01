# 前端开发交接包（P1）

## 1. 目标（给前端团队）
在 1 个 Sprint 内完成 P1 核心前端能力：
1. 微课后即时测（S1）
2. 首页错题入口前置（S2）
3. 连续学习激励展示（S3）

## 2. 页面与组件范围

| 模块 | 页面/组件 | 目标 | 优先级 |
|---|---|---|---|
| 微课后即时测 | `QuizModal`, `QuizQuestionCard`, `QuizResultPanel` | 完成 3 题测验链路 | P0 |
| 错题入口前置 | `HomeWrongbookCard` | 首页显著入口与空状态 | P0 |
| 连续学习激励 | `StreakBadge`, `RewardToast` | 连续学习反馈与奖励提示 | P1 |

## 3. 交互状态定义（必须支持）

### 3.1 即时测（S1）
- `idle`：待触发（课程未结束）
- `ready`：课程结束，弹出测验
- `answering`：答题中
- `submitted`：单题提交反馈
- `completed`：全部题目提交完成
- `error`：提交异常（可重试）

### 3.2 错题入口（S2）
- `has_items`：显示待复习数量
- `empty`：显示“今日无错题”提示
- `loading`：数据加载中
- `error`：拉取失败提示与重试

### 3.3 激励（S3）
- `in_progress`：连续学习进行中
- `achieved`：达标可领奖
- `claimed`：奖励已领取
- `muted`：用户关闭提醒

## 4. 接口契约（前端字段）

### 4.1 获取即时测题目
`GET /api/v1/quiz/{lesson_id}`

```json
{
  "quiz_id": "quiz_001",
  "lesson_id": "lesson_101",
  "questions": [
    {"question_id": "q1", "stem": "...", "options": ["A","B","C"], "answer_type": "single"}
  ]
}
```

### 4.2 提交答题
`POST /api/v1/quiz/{quiz_id}/submit`

```json
{
  "user_id": "u_001",
  "question_id": "q1",
  "selected_option": "B"
}
```

响应：
```json
{
  "is_correct": true,
  "explanation": "..."
}
```

### 4.3 获取错题概览
`GET /api/v1/wrongbook/summary?user_id=u_001`

```json
{
  "wrong_count_today": 5
}
```

### 4.4 连续学习状态
`GET /api/v1/streak/status?user_id=u_001`

```json
{
  "streak_days": 6,
  "reward_available": false,
  "muted": false
}
```

## 5. 埋点要求（前端必打）
- `quiz_start`
- `quiz_submit`
- `quiz_complete`
- `wrongbook_entry_click`
- `streak_progress`
- `streak_reward_claim`

## 6. 验收清单（前端）
- [ ] S1 全链路完成（正常/异常/重试）
- [ ] S2 首页入口状态完整（has_items/empty/loading/error）
- [ ] S3 激励状态完整（in_progress/achieved/claimed/muted）
- [ ] 所有埋点事件可在测试环境观测
- [ ] UI 在 360px 宽度下不破版

## 7. 建议开发顺序（最快落地）
1. S1 基础链路（先可用）
2. S2 首页入口前置
3. S1 体验优化（解释文案、错误重试）
4. S3 激励反馈
