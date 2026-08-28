#!/usr/bin/env python3
"""Create a non-destructive scaffold for a Feynman learning project."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


def write_if_missing(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--topic", required=True)
    args = parser.parse_args()

    root = args.project_dir.expanduser()
    if root.exists() and not root.is_dir():
        parser.error(f"project path is not a directory: {root}")
    if root.exists() and any(root.iterdir()) and not (root / "00-project.md").exists():
        parser.error(f"refusing to initialize a non-empty, unrelated directory: {root}")

    root.mkdir(parents=True, exist_ok=True)
    for relative in (
        "02-materials",
        "03-modules",
        "04-assessments",
        "05-progress",
        "06-sessions",
    ):
        (root / relative).mkdir(exist_ok=True)

    today = date.today().isoformat()
    write_if_missing(
        root / "00-project.md",
        f"""# 学习项目：{args.topic}\n\n主题：{args.topic}\n用户目标：\n当前基础：\n期望深度：\n时间约束：\n语言与表达偏好：\n资料边界：\n实践要求：\n创建时间：{today}\n最后更新时间：{today}\n""",
    )
    write_if_missing(
        root / "01-roadmap.md",
        f"""# 学习路线图：{args.topic}\n\n> 由 feynman-learning 根据用户目标生成；此处不把空模板视为已规划。\n\n模块列表：\n\n| 模块 | 能力目标 | 前置 | 状态 | 最新掌握率 |\n| --- | --- | --- | --- | --- |\n""",
    )
    write_if_missing(
        root / "02-materials" / "index.md",
        """# 学习资料索引\n\n| 资料 | 来源 | 用途 | 适用模块 | 可信度 | 访问日期 |\n| --- | --- | --- | --- | --- | --- |\n""",
    )
    write_if_missing(
        root / "05-progress" / "progress.md",
        """# 学习进度\n\ncurrent_module: 待规划\ncurrent_state: planned\n总体完成率: 0%\n最后更新时间: """ + today + "\n\n| 模块 | 状态 | 最新掌握率 | 最近检测 | 薄弱点 | 下一动作 |\n| --- | --- | --- | --- | --- | --- |\n",
    )
    write_if_missing(root / "05-progress" / "changelog.md", "# 变更日志\n\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
