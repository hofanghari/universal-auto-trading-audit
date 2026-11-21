# Phase 4 — Continuous System Audit

## Objective
Detect newly introduced defects, regressions, integrity drift and operational
degradation after changes or on a scheduled cadence.

## Baseline
Use the latest independently verified baseline. Record its audit run ID,
commit/revision, schema version, configuration version and date. If no valid
baseline exists, state that and perform a scoped Phase 1 baseline audit.

## Trigger conditions
Run an appropriate continuous audit after:
- code or dependency changes;
- database schema/migration changes;
- strategy or risk-rule changes;
- exchange/provider/API integration changes;
- dashboard/reporting changes;
- deployment or infrastructure changes;
- incidents, unusual errors, or scheduled review intervals.

## Procedure
1. Identify changes since baseline (Git diff, migrations, config, dependencies).
2. Map changed components to dependent workflows and UI elements.
3. Select tests based on impact and risk.
4. Check trading state transitions, calculations, order/trade reconciliation,
   data freshness, DB integrity, API contracts and dashboard consistency.
5. Inspect logs, workers, schedules, connections and recovery behavior.
6. Compare behavior and reliability against baseline; distinguish legitimate
   strategy/performance variation from software defects.
7. Detect recurrence of resolved Finding IDs and create new findings as needed.
8. Update ledger, register, report and baseline only after verification.

## Alert policy
Critical/High findings: promptly alert the responsible operator, preserve
evidence, recommend safe containment, and do not make unauthorized production
changes. Medium/Low findings: add prioritized backlog items.

Automatic remediation is permitted only when explicitly authorized, narrowly
scoped, reversible, tested, and protected by defined safeguards.

## Required report
`CONTINUOUS_AUDIT_REPORT.md` includes audit window, baseline, changes, scope,
new findings, regressions, data integrity, trading logic, API/dashboard results,
tests, reliability trends, unresolved risks and actions.

Never erase resolved historical findings. Track recurrence and full lifecycle.
