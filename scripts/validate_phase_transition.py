#!/usr/bin/env python3
"""Conservative phase transition guard based on ledger phase states."""
import argparse, json, sys
from pathlib import Path

ORDER = ["PHASE_1", "PHASE_2", "PHASE_3", "PHASE_4"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phase_status_json")
    ap.add_argument("--to", required=True, choices=ORDER)
    args = ap.parse_args()
    try:
        data = json.loads(Path(args.phase_status_json).read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot read phase status: {exc}")
        return 2
    idx = ORDER.index(args.to)
    if idx == 0:
        print("PASS: Phase 1 has no prior phase prerequisite (preflight still required).")
        return 0
    previous = ORDER[idx - 1]
    prev = data.get("phases", {}).get(previous, {})
    status, gate = prev.get("status"), prev.get("gate")
    accepted = {"PHASE_1": {"COMPLETED"}, "PHASE_2": {"COMPLETED"},
                "PHASE_3": {"ACCEPTED", "CONDITIONALLY_ACCEPTED"},
                "PHASE_4": {"COMPLETED"}}
    if status not in accepted.get(previous, set()):
        print(f"BLOCKED: {previous} status={status!r} is not an allowed predecessor.")
        return 1
    if gate not in {"PASS", "ACCEPTED", "CONDITIONALLY_ACCEPTED"}:
        print(f"BLOCKED: {previous} gate={gate!r} is not passing.")
        return 1
    print(f"PASS: transition prerequisite {previous} -> {args.to} is structurally satisfied.")
    print("Note: this script validates recorded state only; it cannot prove evidence is genuine.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
