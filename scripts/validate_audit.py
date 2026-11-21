#!/usr/bin/env python3
"""Basic structural validator for a Universal Auto Trading Audit run."""
import argparse, json, sys
from pathlib import Path

VALID_ITEM = {"NOT_STARTED", "IN_PROGRESS", "COMPLETED", "BLOCKED",
              "NOT_APPLICABLE", "NOT_TESTED", "INCONCLUSIVE"}
VALID_GATE = {"PASS", "FAIL", "BLOCKED", "NOT_EVALUABLE"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ledger", help="Path to execution_ledger.json")
    ap.add_argument("--findings", help="Optional finding_register.json")
    args = ap.parse_args()
    errors, warnings = [], []
    p = Path(args.ledger)
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"FAIL: cannot read ledger: {exc}")
        return 2
    for key in ("run_id", "active_phase", "phase_status", "items", "gate_result"):
        if key not in data:
            errors.append(f"Missing ledger key: {key}")
    if data.get("gate_result") not in VALID_GATE:
        errors.append("Invalid or missing gate_result")
    seen = set()
    for i, item in enumerate(data.get("items", [])):
        tid = item.get("task_id")
        if not tid:
            errors.append(f"Item {i} has no task_id")
        elif tid in seen:
            errors.append(f"Duplicate task_id: {tid}")
        seen.add(tid)
        status = item.get("status")
        if status not in VALID_ITEM:
            errors.append(f"{tid}: invalid status {status}")
        if status == "COMPLETED" and not item.get("evidence"):
            errors.append(f"{tid}: COMPLETED without evidence")
        if status == "NOT_APPLICABLE" and not item.get("notes"):
            errors.append(f"{tid}: NOT_APPLICABLE requires justification in notes")
        if status == "BLOCKED" and not item.get("blocker") and not item.get("notes"):
            errors.append(f"{tid}: BLOCKED requires blocker/notes")
    if args.findings:
        try:
            fd = json.loads(Path(args.findings).read_text(encoding="utf-8"))
            ids = set()
            for f in fd.get("findings", []):
                fid = f.get("finding_id")
                if not fid or fid in ids:
                    errors.append(f"Missing or duplicate finding_id: {fid}")
                ids.add(fid)
                if f.get("status") == "VERIFIED_FIXED" and not f.get("verification_evidence"):
                    errors.append(f"{fid}: VERIFIED_FIXED without verification_evidence")
        except Exception as exc:
            errors.append(f"Cannot read findings: {exc}")
    completed = sum(x.get("status") == "COMPLETED" for x in data.get("items", []))
    blocked = sum(x.get("status") == "BLOCKED" for x in data.get("items", []))
    untested = sum(x.get("status") in {"NOT_TESTED", "INCONCLUSIVE"} for x in data.get("items", []))
    print(f"Items: {len(data.get('items', []))}; completed={completed}; blocked={blocked}; not_tested/inconclusive={untested}")
    if warnings:
        for w in warnings: print("WARNING:", w)
    if errors:
        for e in errors: print("ERROR:", e)
        print("VALIDATION: FAIL")
        return 1
    print("VALIDATION: PASS (structural checks only; not proof of system correctness)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
