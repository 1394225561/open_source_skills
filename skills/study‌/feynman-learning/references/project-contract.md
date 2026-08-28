# 学习项目契约

## 状态值

项目和模块使用以下状态：

- `planned`：已规划，尚未开始
- `in_progress`：正在学习材料或练习
- `assessment_pending`：材料已学完，等待用户检测回答
- `remediation`：最近一次检测低于 80%，正在补救
- `mastered`：最近一次检测达到至少 80%
- `paused`：用户要求暂停，必须记录恢复点
- `completed`：项目综合任务通过

状态转换必须有事件证据：

```text
planned -> in_progress -> assessment_pending
assessment_pending -> mastered
assessment_pending -> remediation -> assessment_pending
mastered -> in_progress (进入后续模块)
任意状态 -> paused (用户明确暂停)
```

## 文件字段

`00-project.md` 至少包含：主题、用户目标、目标读者/使用场景、当前基础、期望深度、时间约束、语言与表达偏好、资料边界、实践要求、创建时间、最后更新时间。

`01-roadmap.md` 的每个模块至少包含：编号和名称、能力目标、前置关系、学习材料路径、练习、检测评分点、掌握门槛、状态、最近掌握率。

`03-modules/module-XX.md` 至少包含：

```text
目标：
前置：
核心概念：
必须能解释：
必须能应用：
边界/反例：
常见误区：
练习：
检测评分点：
状态：
已掌握点：
薄弱点：
下一动作：
```

`04-assessments/module-XX-attempt-YY.md` 必须保留不可变的原始记录：检测时间、题目、用户原答、逐点评分、总分、掌握率、证据、错误类型、补救方案、是否允许推进。修订后的解释写在后面，不覆盖原答或原分数。

`05-progress/progress.md` 使用简短表格维护：模块、状态、最新掌握率、最近检测、薄弱点、下一动作；顶部写 `current_module`、`current_state`、总体完成率和更新时间。

`05-progress/changelog.md` 只追加不改写，格式为：

```text
## YYYY-MM-DD HH:MM
- 事件：
- 证据：
- 决定：
- 下一步：
```

## 资料要求

材料不是资料堆积。每个模块讲义应尽量包含：先验唤醒、直观解释、准确模型、最小示例、反例/边界、迁移练习和来源。资料索引中的来源按“权威原始来源 > 高质量教材/课程 > 可靠综述 > 一般博客/论坛”标注等级；低等级内容不能独自支撑关键事实。
