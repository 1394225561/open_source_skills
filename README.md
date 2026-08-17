# Open Source Skills

面向 Codex 和兼容 [Agent Skills](https://agentskills.io/) 规范的开源 Skill 集合。

## 安装

列出仓库中的可用 Skill：

```bash
npx skills add 1394225561/open_source_skills --list
```

安装指定 Skill：

```bash
npx skills add 1394225561/open_source_skills --skill novel-orchestrator
```

只安装到 Codex：

```bash
npx skills add 1394225561/open_source_skills \
  --skill novel-orchestrator \
  --agent codex
```

## Skill 目录

### 小说创作

| Skill | 说明 | 依赖 |
| --- | --- | --- |
| `novel-orchestrator` | 编排中文小说的策划、创作、连续性审校与全稿修订 | 当前会话须已加载 `chinese-novelist` |

仓库按领域分类存放 Skill，例如小说相关 Skill 位于 `skills/novel/`。分类目录只用于组织源码，不改变 Skill 名称或安装方式。

## 兼容性

- Codex
- 支持 Agent Skills 规范的其他 Agent

不同 Agent 对可选元数据和工具调用的支持可能不同。每个 Skill 的具体依赖以其 `SKILL.md` 为准。

## License

[MIT](LICENSE)
