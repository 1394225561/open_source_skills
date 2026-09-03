#!/usr/bin/env python3
"""Create and version a traceable self-media content workspace."""

from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path


LEDGER_FIELDS = [
    "topic_id",
    "title",
    "platform",
    "format",
    "goal",
    "status",
    "current_version",
    "published_version",
    "created_at",
    "published_at",
    "post_url",
]

FEEDBACK_FIELDS = [
    "recorded_at",
    "observation_window",
    "platform",
    "published_version",
    "impressions",
    "views_or_reads",
    "avg_watch_or_read",
    "completion_rate",
    "likes",
    "comments",
    "saves",
    "shares",
    "profile_visits",
    "follows",
    "direct_messages",
    "leads",
    "conversions",
    "revenue",
    "qualitative_notes",
]


def now() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def safe_directory_name(value: str) -> str:
    value = value.strip()
    value = re.sub(r"[\\/:*?\"<>|\x00-\x1f]+", "-", value)
    value = re.sub(r"\s+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-. ")
    if not value or value in {".", ".."}:
        raise ValueError("目录名清理后为空，请提供更具体的赛道或 --directory。")
    return value[:80].rstrip("-. ")


def write_text(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def write_csv_header(path: Path, fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=fields).writeheader()


def load_workspace(path: str) -> tuple[Path, dict]:
    root = Path(path).expanduser().resolve()
    metadata_path = root / "workspace.json"
    if not metadata_path.is_file():
        raise ValueError(f"不是有效工作区，缺少 {metadata_path}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if metadata.get("schema_version") != 1:
        raise ValueError("不支持的工作区 schema_version。")
    return root, metadata


def create_workspace(args: argparse.Namespace) -> None:
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"根目录不存在或不是目录：{root}")

    directory = safe_directory_name(args.directory or f"{args.niche}-自媒体")
    target = root / directory
    if target.exists():
        raise FileExistsError(f"目标已存在，拒绝覆盖：{target}")

    (target / "topics").mkdir(parents=True)
    created_at = now()
    metadata = {
        "schema_version": 1,
        "niche": args.niche.strip(),
        "created_at": created_at,
        "topic_id_format": "TYYYYMMDD-NNN",
    }
    write_text(target / "workspace.json", json.dumps(metadata, ensure_ascii=False, indent=2))
    write_text(
        target / "工作区说明.md",
        f"""# {args.niche.strip()}自媒体工作区

本目录记录选题、内容版本、发布产物和反馈。不要覆盖已经发布的版本；新建选题和版本使用 Skill 自带脚本。

- 创建时间：{created_at}
- 结构版本：1
- 当前阶段：等待填写赛道档案和初版选题棋盘
""",
    )
    write_text(
        target / "赛道档案.md",
        f"""# 赛道档案

## 已确认事实

- 赛道：{args.niche.strip()}

## 暂定假设

- 目标受众：待补充
- 核心问题/期待结果：待补充
- 主要平台：待补充
- 内容形态：待补充
- 商业承接：待补充

## 可用证据资产

| 资产 | 来源/位置 | 可支持的主张 | 使用授权 | 状态 |
|---|---|---|---|---|
| 待补充 | | | | 待核验 |

## 内容边界与禁区

- 待补充

## 修订记录

| 日期 | 改动 | 依据 |
|---|---|---|
| {created_at} | 建立赛道档案 | 用户提供赛道 |
""",
    )
    rows = []
    for row in "ABCDE":
        cells = []
        for col in range(1, 6):
            if row == "C" and col == 3:
                cells.append(args.niche.strip())
            elif row in "BD" and col in (2, 3, 4) or row == "C" and col in (2, 4):
                cells.append("内圈待拟定")
            else:
                cells.append("外圈待拟定")
        rows.append(f"| {row} | " + " | ".join(cells) + " |")
    board = "\n".join(rows)
    write_text(
        target / "选题棋盘.md",
        f"""# 选题棋盘

## 5x5 棋盘

|  | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
{board}

## 严格射线候选

| 编号 | 中心 | 内圈 | 外圈锚点 | 一句话方向 | 选择理由 |
|---|---|---|---|---|---|
| 待拟定 | {args.niche.strip()} | | | | |

## 扩展场景候选

| 编号 | 中心 | 内圈 | 外圈场景 | 一句话方向 | 选择理由 |
|---|---|---|---|---|---|
| 待拟定 | {args.niche.strip()} | | | | |

## 修订记录

| 日期 | 改动 | 依据 | 影响路径 |
|---|---|---|---|
| {created_at} | 初始化棋盘 | 用户提供赛道 | 全部 |
""",
    )
    write_csv_header(target / "选题台账.csv", LEDGER_FIELDS)
    write_text(
        target / "运营实验.md",
        """# 运营实验

| 实验编号 | 来源选题 | 假设 | 只改变的变量 | 成功信号 | 观察窗口 | 结果 | 决策 |
|---|---|---|---|---|---|---|---|
""",
    )
    print(target)


def next_topic_id(ledger_path: Path) -> str:
    date_key = datetime.now().strftime("%Y%m%d")
    pattern = re.compile(rf"^T{date_key}-(\d{{3}})$")
    highest = 0
    with ledger_path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            match = pattern.match(row.get("topic_id", ""))
            if match:
                highest = max(highest, int(match.group(1)))
    return f"T{date_key}-{highest + 1:03d}"


def create_topic(args: argparse.Namespace) -> None:
    root, metadata = load_workspace(args.workspace)
    ledger_path = root / "选题台账.csv"
    topic_id = next_topic_id(ledger_path)
    topic_root = root / "topics" / topic_id
    version_root = topic_root / "versions" / "v001"
    version_root.mkdir(parents=True)
    created_at = now()

    write_text(
        topic_root / "选题简报.md",
        f"""# {topic_id} 选题简报

- 题目：{args.title}
- 赛道：{metadata['niche']}
- 平台：{args.platform}
- 形态：{args.format}
- 主要目标：{args.goal}
- 创建时间：{created_at}

## 用户确认原话

- 待补充

## 诊断链

- 目标人群：待补充
- 具体场景：待补充
- 可感症状：待补充
- 旧解释：待补充
- 隐藏原因：待补充
- 继续成本：待补充
- 可执行下一步：待补充
- 单一 CTA：待补充

## 证据、来源与边界

| 主张 | 证据/来源 | 检索日期 | 强度与限制 | 状态 |
|---|---|---|---|---|
| 待补充 | | | | 待核验 |

## 成功信号

- 待补充
""",
    )
    write_text(
        topic_root / "变更记录.md",
        f"""# 变更记录

| 版本 | 时间 | 修改目的 | 依据 | 实际变化 |
|---|---|---|---|---|
| v001 | {created_at} | 建立首版 | 用户确认选题 | 待创作 |
""",
    )
    write_csv_header(topic_root / "反馈.csv", FEEDBACK_FIELDS)
    write_text(
        topic_root / "复盘.md",
        """# 复盘

## 事实

待发布后填写。

## 解释

待填写，并标注信心高/中/低。

## 判断

待填写。

## 动作

待填写。

## 下一测试

待填写。
""",
    )
    for filename, heading in (
        ("正文.md", "正文"),
        ("制作单.md", "制作单"),
        ("发布包.md", "发布包"),
    ):
        write_text(
            version_root / filename,
            f"# {topic_id} v001 {heading}\n\n- 状态：待填写\n",
        )

    row = {
        "topic_id": topic_id,
        "title": args.title,
        "platform": args.platform,
        "format": args.format,
        "goal": args.goal,
        "status": "selected",
        "current_version": "v001",
        "published_version": "",
        "created_at": created_at,
        "published_at": "",
        "post_url": "",
    }
    with ledger_path.open("a", encoding="utf-8", newline="") as handle:
        csv.DictWriter(handle, fieldnames=LEDGER_FIELDS).writerow(row)
    print(topic_root)


def read_ledger(path: Path) -> list[dict]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_ledger(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=LEDGER_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def create_version(args: argparse.Namespace) -> None:
    root, _ = load_workspace(args.workspace)
    if not re.fullmatch(r"T\d{8}-\d{3}", args.topic_id):
        raise ValueError("topic-id 格式必须为 TYYYYMMDD-NNN。")

    ledger_path = root / "选题台账.csv"
    rows = read_ledger(ledger_path)
    matches = [row for row in rows if row["topic_id"] == args.topic_id]
    if len(matches) != 1:
        raise ValueError(f"台账中未找到唯一选题：{args.topic_id}")
    topic = matches[0]
    current = topic["current_version"]
    if not re.fullmatch(r"v\d{3}", current):
        raise ValueError(f"台账中的 current_version 无效：{current}")

    next_version = f"v{int(current[1:]) + 1:03d}"
    topic_root = root / "topics" / args.topic_id
    source = topic_root / "versions" / current
    target = topic_root / "versions" / next_version
    if not source.is_dir():
        raise ValueError(f"源版本目录不存在：{source}")
    if target.exists():
        raise FileExistsError(f"目标版本已存在，拒绝覆盖：{target}")

    shutil.copytree(source, target)
    topic["current_version"] = next_version
    if topic["status"] in {"ready", "published", "measuring", "iterated"}:
        topic["status"] = "drafting"
    write_ledger(ledger_path, rows)

    changed_at = now()
    with (topic_root / "变更记录.md").open("a", encoding="utf-8") as handle:
        handle.write(
            f"| {next_version} | {changed_at} | {args.summary} | {current} | 待填写 |\n"
        )
    print(target)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="创建新的赛道工作区")
    init_parser.add_argument("--niche", required=True, help="赛道或行业")
    init_parser.add_argument("--root", default=".", help="创建位置，默认当前目录")
    init_parser.add_argument("--directory", help="可选的工作区目录名，不接受路径")
    init_parser.set_defaults(handler=create_workspace)

    topic_parser = subparsers.add_parser("new-topic", help="创建选题档案和 v001")
    topic_parser.add_argument("--workspace", required=True, help="赛道工作区")
    topic_parser.add_argument("--title", required=True, help="确认后的选题标题")
    topic_parser.add_argument("--platform", required=True, help="目标平台")
    topic_parser.add_argument("--format", required=True, help="内容形态")
    topic_parser.add_argument("--goal", required=True, help="主要内容目标")
    topic_parser.set_defaults(handler=create_topic)

    version_parser = subparsers.add_parser("new-version", help="从当前版本创建新版本")
    version_parser.add_argument("--workspace", required=True, help="赛道工作区")
    version_parser.add_argument("--topic-id", required=True, help="选题编号")
    version_parser.add_argument("--summary", required=True, help="本轮修改目的")
    version_parser.set_defaults(handler=create_version)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.handler(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
