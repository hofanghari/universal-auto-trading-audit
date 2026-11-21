# Phase 3 — Independent Verification Audit

## Objective
Independently determine whether remediation works. The implementer’s claim or
test output is evidence to inspect, not a substitute for independent verification.

## Independence
Prefer a different QA/Audit Agent and a clean review context. If the same agent
must verify, disclose the limitation and do not describe the review as fully
independent.

## Verification procedure
For each original Finding ID:
1. Read original finding, acceptance criteria, remediation report, code diff,
   and tests.
2. Independently inspect the changed implementation.
3. Reproduce the original failure scenario safely.
4. Execute relevant tests; record exact command, environment, exit status and
   meaningful output.
5. Verify expected behavior and edge cases.
6. Check adjacent workflows for regression.
7. Reconcile database -> calculation -> API -> frontend/dashboard where relevant.
8. Record evidence and limitations.

## Minimum regression areas
Consider normal flows, missing/empty data, duplicate/delayed events, reconnects,
timeouts, API errors, DB failures/recovery, concurrency, restarts, boundary
values, historical queries, timezones, refresh/filter changes, and partial fills.
Select applicable cases; justify exclusions.

## Dashboard reconciliation
For important metrics:
- define the metric precisely;
- define included/excluded states and time window;
- obtain source records;
- independently calculate expected value;
- compare persisted aggregates, API response, frontend state and display;
- account for rounding, timezone, fees, funding, slippage, open/closed state;
- preserve query/capture evidence without exposing secrets.

## Finding verification statuses
- VERIFIED_FIXED
- PARTIALLY_VERIFIED
- FAILED
- NOT_TESTED
- INCONCLUSIVE

A finding is `VERIFIED_FIXED` only if the acceptance criteria pass with evidence.
Untested or inaccessible behavior cannot be counted as fixed.

## Release recommendation
- ACCEPTED: mandatory criteria pass; no unresolved Critical/High defects.
- CONDITIONALLY_ACCEPTED: only documented, explicitly accepted non-critical risks
  remain, with approver and expiry/mitigation.
- REJECTED: unresolved Critical/High defects or mandatory verification failures.
- NOT_EVALUABLE: insufficient access/evidence to reach a defensible conclusion.

## Required report
`VERIFICATION_REPORT.md` includes:
1. Verification scope and independence statement.
2. Original Finding ID -> status matrix.
3. Test execution evidence.
4. Trading logic and calculation verification.
5. DB/API/dashboard reconciliation.
6. Regression and edge-case results.
7. New findings.
8. Failed/incomplete fixes.
9. Remaining risks and limitations.
10. Release recommendation and rationale.

Never allow the Engineering Agent to self-approve its own fix.
