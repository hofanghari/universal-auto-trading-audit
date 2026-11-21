# Phase 2 — Controlled Remediation

## Objective
Resolve verified findings safely, in prioritized and reviewable batches.

## Inputs
Read the latest `AUDIT_REPORT.md`, finding register, project specifications,
source code, relevant tests, and current Git/worktree state. Reproduce critical
findings before modifying code when feasible.

## Prioritization
1. CRITICAL: data corruption, unauthorized execution risk, unsafe order state,
   severe integrity/security failures, materially wrong financial calculations.
2. HIGH: incorrect trading/business logic, material DB/API/dashboard mismatch,
   broken execution or integration.
3. MEDIUM: functional defects, synchronization, error handling, reliability.
4. LOW: minor UI, maintainability, non-critical performance.

Prioritize by impact and dependencies; do not treat this order as permission to
perform dangerous actions.

## Per-finding workflow
1. Confirm finding and expected behavior.
2. Identify root cause and affected dependencies.
3. Define minimal correction and acceptance test.
4. Check worktree, backup/rollback and environment.
5. Obtain explicit authorization for production writes, destructive changes,
   deployments, strategy/risk changes, or irreversible actions.
6. Implement one coherent batch.
7. Add/update tests.
8. Run targeted tests and relevant regression tests.
9. Inspect logs, database integrity, API output and affected UI.
10. Record changed files, commands, results, evidence, and residual risks.

## Rules
- Do not change strategy, indicators, filters, parameters, or risk rules unless
  explicitly authorized.
- Do not optimize historical results by tuning parameters during defect repair.
- Do not fabricate or modify historical trade data to make metrics reconcile.
- Do not replace real data with mocks outside isolated tests.
- Preserve compatibility and project conventions.
- Avoid broad rewrites; isolate changes.
- Stop the batch if unexpected regression or data risk appears.
- Never send real orders or use real funds.
- Use fixtures/sandbox/paper mode for execution tests.
- If the fix cannot be safely verified, mark it NOT VERIFIED.

## Status values
`RESOLVED_PENDING_VERIFICATION`, `PARTIALLY_RESOLVED`, `NOT_RESOLVED`,
`BLOCKED`, `NOT_TESTED`.

Only the independent Phase 3 process may mark a finding `VERIFIED_FIXED`.

## Required report
`REMEDIATION_REPORT.md` must map every original Finding ID to:
- action taken;
- files changed;
- implementation summary;
- tests executed and exact results;
- database/API/UI checks;
- regression results;
- remaining work and risks;
- commit/change reference where available.

## Exit criteria
All assigned findings have an explicit status, all changes are traceable, tests
are reported truthfully, and unresolved items are carried forward. Phase 2 does
not grant acceptance.
