#!/usr/bin/env python3
"""Validate the deterministic state contract of a novel project.

This script checks file presence, JSON shape, identifiers, chapter ordering, and
explicitly open blockers. It does not score prose or claim literary quality.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_MARKDOWN = (
    "03-故事圣经.md",
    "04-剧情工程.md",
    "07-场景计划.md",
    "08-质量报告.md",
    "09-修订计划.md",
)
CONTINUITY_FILE = "05-连续性账本.json"
THREAD_FILE = "06-线索与承诺账本.json"
ISSUE_SEVERITIES = {"blocker", "major", "minor"}
ISSUE_STATUSES = {"open", "resolved", "accepted"}
THREAD_TYPES = {
    "plot",
    "clue",
    "foreshadow",
    "relationship",
    "theme",
    "reader-promise",
}
THREAD_STATUSES = {
    "planned",
    "open",
    "advanced",
    "resolved",
    "intentionally-open",
}


def is_integer(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def require_keys(
    item: dict[str, Any],
    keys: tuple[str, ...],
    location: str,
    errors: list[str],
) -> None:
    for key in keys:
        if key not in item:
            errors.append(f"{location}: missing key '{key}'")


def check_unique_id(
    value: Any,
    seen: set[str],
    location: str,
    errors: list[str],
) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{location}: ID must be a non-empty string")
    elif value in seen:
        errors.append(f"{location}: duplicate ID '{value}'")
    else:
        seen.add(value)


def validate_continuity(data: Any) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    max_chapter = 0
    if not isinstance(data, dict):
        return ["continuity ledger: root must be an object"], warnings, max_chapter

    require_keys(
        data,
        (
            "schema_version",
            "updated_through_chapter",
            "timeline",
            "characters",
            "world_facts",
            "continuity_issues",
        ),
        "continuity ledger",
        errors,
    )
    if data.get("schema_version") != 1:
        errors.append("continuity ledger: schema_version must be 1")

    updated = data.get("updated_through_chapter")
    if not is_integer(updated) or updated < 0:
        errors.append("continuity ledger: updated_through_chapter must be a non-negative integer")
    else:
        max_chapter = max(max_chapter, updated)

    timeline = data.get("timeline")
    event_ids: set[str] = set()
    if not isinstance(timeline, list):
        errors.append("continuity ledger: timeline must be an array")
    else:
        for index, event in enumerate(timeline):
            location = f"timeline[{index}]"
            if not isinstance(event, dict):
                errors.append(f"{location}: event must be an object")
                continue
            require_keys(
                event,
                (
                    "event_id",
                    "chapter",
                    "order",
                    "time",
                    "location",
                    "participants",
                    "cause",
                    "effects",
                ),
                location,
                errors,
            )
            check_unique_id(event.get("event_id"), event_ids, location, errors)
            chapter = event.get("chapter")
            if not is_integer(chapter) or chapter < 1:
                errors.append(f"{location}: chapter must be a positive integer")
            else:
                max_chapter = max(max_chapter, chapter)
            if not is_integer(event.get("order")) or event.get("order", 0) < 1:
                errors.append(f"{location}: order must be a positive integer")
            for key in ("participants", "cause", "effects"):
                if not isinstance(event.get(key), list):
                    errors.append(f"{location}: {key} must be an array")

    characters = data.get("characters")
    if not isinstance(characters, dict):
        errors.append("continuity ledger: characters must be an object keyed by stable character ID")
    else:
        for character_id, character in characters.items():
            location = f"characters.{character_id}"
            if not isinstance(character_id, str) or not character_id.strip():
                errors.append(f"{location}: character ID must be a non-empty string")
            if not isinstance(character, dict):
                errors.append(f"{location}: character state must be an object")
                continue
            require_keys(
                character,
                (
                    "name",
                    "aliases",
                    "location",
                    "physical_state",
                    "emotional_state",
                    "relationships",
                    "knowledge",
                    "inventory",
                    "goals",
                    "last_updated_chapter",
                ),
                location,
                errors,
            )
            last_chapter = character.get("last_updated_chapter")
            if not is_integer(last_chapter) or last_chapter < 0:
                errors.append(f"{location}: last_updated_chapter must be a non-negative integer")
            else:
                max_chapter = max(max_chapter, last_chapter)
            for key in ("aliases", "knowledge", "inventory", "goals"):
                if not isinstance(character.get(key), list):
                    errors.append(f"{location}: {key} must be an array")
            if not isinstance(character.get("relationships"), dict):
                errors.append(f"{location}: relationships must be an object")

    facts = data.get("world_facts")
    fact_ids: set[str] = set()
    if not isinstance(facts, list):
        errors.append("continuity ledger: world_facts must be an array")
    else:
        for index, fact in enumerate(facts):
            location = f"world_facts[{index}]"
            if not isinstance(fact, dict):
                errors.append(f"{location}: fact must be an object")
                continue
            require_keys(
                fact,
                ("fact_id", "statement", "introduced_chapter", "status"),
                location,
                errors,
            )
            check_unique_id(fact.get("fact_id"), fact_ids, location, errors)
            chapter = fact.get("introduced_chapter")
            if not is_integer(chapter) or chapter < 0:
                errors.append(f"{location}: introduced_chapter must be a non-negative integer")
            else:
                max_chapter = max(max_chapter, chapter)

    issues = data.get("continuity_issues")
    issue_ids: set[str] = set()
    if not isinstance(issues, list):
        errors.append("continuity ledger: continuity_issues must be an array")
    else:
        for index, issue in enumerate(issues):
            location = f"continuity_issues[{index}]"
            if not isinstance(issue, dict):
                errors.append(f"{location}: issue must be an object")
                continue
            require_keys(
                issue,
                (
                    "issue_id",
                    "severity",
                    "status",
                    "chapters",
                    "description",
                    "resolution",
                ),
                location,
                errors,
            )
            check_unique_id(issue.get("issue_id"), issue_ids, location, errors)
            severity = issue.get("severity")
            status = issue.get("status")
            if severity not in ISSUE_SEVERITIES:
                errors.append(f"{location}: invalid severity '{severity}'")
            if status not in ISSUE_STATUSES:
                errors.append(f"{location}: invalid status '{status}'")
            if not isinstance(issue.get("chapters"), list):
                errors.append(f"{location}: chapters must be an array")
            if severity == "blocker" and status == "open":
                errors.append(f"{location}: open blocker prevents continuation")
            if status in {"resolved", "accepted"} and not str(issue.get("resolution", "")).strip():
                errors.append(f"{location}: {status} issue requires a resolution")
            if severity == "blocker" and status == "accepted":
                warnings.append(f"{location}: accepted blocker requires explicit author intent")

    if is_integer(updated) and max_chapter > updated:
        warnings.append(
            "continuity ledger: entries reference chapters beyond updated_through_chapter"
        )
    return errors, warnings, max_chapter


def validate_threads(data: Any) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warnings: list[str] = []
    max_chapter = 0
    if not isinstance(data, dict):
        return ["thread ledger: root must be an object"], warnings, max_chapter
    require_keys(data, ("schema_version", "threads"), "thread ledger", errors)
    if data.get("schema_version") != 1:
        errors.append("thread ledger: schema_version must be 1")
    threads = data.get("threads")
    if not isinstance(threads, list):
        return errors + ["thread ledger: threads must be an array"], warnings, max_chapter

    thread_ids: set[str] = set()
    for index, thread in enumerate(threads):
        location = f"threads[{index}]"
        if not isinstance(thread, dict):
            errors.append(f"{location}: thread must be an object")
            continue
        require_keys(
            thread,
            (
                "thread_id",
                "type",
                "description",
                "planted_chapter",
                "target_payoff_chapter",
                "resolved_chapter",
                "status",
                "evidence",
                "notes",
            ),
            location,
            errors,
        )
        check_unique_id(thread.get("thread_id"), thread_ids, location, errors)
        if thread.get("type") not in THREAD_TYPES:
            errors.append(f"{location}: invalid type '{thread.get('type')}'")
        status = thread.get("status")
        if status not in THREAD_STATUSES:
            errors.append(f"{location}: invalid status '{status}'")

        chapter_values: dict[str, int | None] = {}
        for key in ("planted_chapter", "target_payoff_chapter", "resolved_chapter"):
            value = thread.get(key)
            if value is not None and (not is_integer(value) or value < 1):
                errors.append(f"{location}: {key} must be null or a positive integer")
                chapter_values[key] = None
            else:
                chapter_values[key] = value
                if is_integer(value):
                    max_chapter = max(max_chapter, value)

        planted = chapter_values["planted_chapter"]
        target = chapter_values["target_payoff_chapter"]
        resolved = chapter_values["resolved_chapter"]
        if planted and target and target < planted:
            errors.append(f"{location}: target payoff precedes planting")
        if planted and resolved and resolved < planted:
            errors.append(f"{location}: resolution precedes planting")
        if status == "planned" and planted is not None:
            warnings.append(f"{location}: planned thread already has planted_chapter")
        if status in {"open", "advanced"} and planted is None:
            errors.append(f"{location}: {status} thread requires planted_chapter")
        if status == "resolved" and resolved is None:
            errors.append(f"{location}: resolved thread requires resolved_chapter")
        if status != "resolved" and resolved is not None:
            errors.append(f"{location}: only resolved threads may set resolved_chapter")
        if status == "intentionally-open" and not str(thread.get("notes", "")).strip():
            errors.append(f"{location}: intentionally-open thread requires explanatory notes")
        if not isinstance(thread.get("evidence"), list):
            errors.append(f"{location}: evidence must be an array")

    return errors, warnings, max_chapter


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        errors.append(f"missing required file: {path.name}")
    except json.JSONDecodeError as exc:
        errors.append(f"{path.name}: invalid JSON at line {exc.lineno}, column {exc.colno}")
    except OSError as exc:
        errors.append(f"{path.name}: cannot read file: {exc}")
    return None


def validate_project(project: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not project.is_dir():
        return [f"project directory not found: {project}"], warnings

    for filename in REQUIRED_MARKDOWN:
        path = project / filename
        if not path.is_file():
            errors.append(f"missing required file: {filename}")
        elif not path.read_text(encoding="utf-8-sig").strip():
            errors.append(f"required file is empty: {filename}")

    continuity = load_json(project / CONTINUITY_FILE, errors)
    threads = load_json(project / THREAD_FILE, errors)
    max_referenced_chapter = 0
    if continuity is not None:
        found_errors, found_warnings, max_chapter = validate_continuity(continuity)
        errors.extend(found_errors)
        warnings.extend(found_warnings)
        max_referenced_chapter = max(max_referenced_chapter, max_chapter)
    if threads is not None:
        found_errors, found_warnings, max_chapter = validate_threads(threads)
        errors.extend(found_errors)
        warnings.extend(found_warnings)
        max_referenced_chapter = max(max_referenced_chapter, max_chapter)

    plan_path = project / "02-写作计划.json"
    if plan_path.is_file():
        plan = load_json(plan_path, errors)
        if isinstance(plan, dict):
            total = plan.get("totalChapters")
            if is_integer(total) and total > 0 and max_referenced_chapter > total:
                errors.append(
                    "ledgers reference a chapter beyond 02-写作计划.json totalChapters"
                )
    else:
        warnings.append("02-写作计划.json not found; chapter upper bound was not checked")

    return errors, warnings


def run_self_test() -> int:
    continuity = {
        "schema_version": 1,
        "updated_through_chapter": 1,
        "timeline": [
            {
                "event_id": "E001",
                "chapter": 1,
                "order": 1,
                "time": "day 1",
                "location": "station",
                "participants": ["C001"],
                "cause": [],
                "effects": ["C001 learns the train is cancelled"],
            }
        ],
        "characters": {
            "C001": {
                "name": "Test",
                "aliases": [],
                "location": "station",
                "physical_state": "healthy",
                "emotional_state": "concerned",
                "relationships": {},
                "knowledge": ["K001: train cancelled in chapter 1"],
                "inventory": [],
                "goals": ["find another route"],
                "last_updated_chapter": 1,
            }
        },
        "world_facts": [
            {
                "fact_id": "W001",
                "statement": "The last train leaves at midnight.",
                "introduced_chapter": 1,
                "status": "active",
            }
        ],
        "continuity_issues": [],
    }
    threads = {
        "schema_version": 1,
        "threads": [
            {
                "thread_id": "T001",
                "type": "plot",
                "description": "Find another route",
                "planted_chapter": 1,
                "target_payoff_chapter": 2,
                "resolved_chapter": None,
                "status": "open",
                "evidence": ["chapter 1: train cancelled"],
                "notes": "",
            }
        ],
    }
    errors_a, _, _ = validate_continuity(continuity)
    errors_b, _, _ = validate_threads(threads)
    if errors_a or errors_b:
        print("SELF-TEST FAILED")
        for error in errors_a + errors_b:
            print(f"ERROR: {error}")
        return 1

    continuity["continuity_issues"] = [
        {
            "issue_id": "I001",
            "severity": "blocker",
            "status": "open",
            "chapters": [1],
            "description": "Impossible travel",
            "resolution": "",
        }
    ]
    negative_errors, _, _ = validate_continuity(continuity)
    if not any("open blocker" in error for error in negative_errors):
        print("SELF-TEST FAILED: negative case was not detected")
        return 1
    print("SELF-TEST PASSED")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", nargs="?", type=Path, help="novel project directory")
    parser.add_argument("--self-test", action="store_true", help="run in-memory tests")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if args.project is None:
        parser.error("project is required unless --self-test is used")

    errors, warnings = validate_project(args.project.resolve())
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASSED: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
