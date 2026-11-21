#!/usr/bin/env python3
"""Check a JSON checklist export for missing statuses/evidence."""
import argparse, json, sys
from pathlib import Path

STATUSES = {"NOT_STARTED", "IN_PROGRESS", "COMPLETED", "BLOCKED",
            "NOT_APPLICABLE", "NOT_TESTED", "INCONCLUSIVE"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("checklist_json")
    args = ap.parse_args()
    try:
        data = json.loads(Path(args.checklist_json).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: {exc}")
        return 2
    items = data if isinstance(data, list) else data.get("items", [])
    errors = []
    for n, item in enumerate(items, 1):
        name = item.get("description") or item.get("item") or item.get("task_id") or f"item-{n}"
        status = item.get("status")
        if status not in STATUSES:
            errors.append(f"{name}: missing/invalid status")
        if status == "COMPLETED" and not item.get("evidence"):
            errors.append(f"{name}: completed without evidence")
        if status == "NOT_APPLICABLE" and not item.get("reason") and not item.get("notes"):
            errors.append(f"{name}: not applicable without reason")
    if errors:
        print("\n".join(errors))
        print("CHECKLIST: FAIL")
        return 1
    print(f"CHECKLIST: PASS ({len(items)} items; structural validation only)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
