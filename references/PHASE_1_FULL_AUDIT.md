# Phase 1 — Full Project Audit

## Objective
Discover and document the real operating condition of the project. This is an
investigation phase, not an automatic rewrite.

## Scope
1. Architecture and codebase: project map, entry points, services, workers,
   modules, dependencies, configuration, dead/duplicate/incomplete code,
   coupling, exception handling, concurrency, resource lifecycle.
2. Trading/business logic: strategy specification versus implementation,
   signal lifecycle, validation, entry/exit, Long/Short symmetry, order lifecycle,
   TP/SL, position sizing, risk, fees, funding, slippage, PnL, state transitions,
   idempotency, duplicate signals/orders, lookahead/data leakage where relevant.
3. Data feeds: exchange/provider contracts, WebSocket/REST handling, candle
   completeness, symbol mapping, precision, timestamps, timezone, stale data,
   reconnect/retry, rate limits, gap detection, source separation.
4. Database: schema, migrations, keys, constraints, indexes, transactions,
   consistency, duplicate/missing records, state transitions, retention, backup
   and recovery assumptions. Prefer read-only queries.
5. Backend/API: endpoint inventory, contracts, validation, pagination, filters,
   aggregation, caching, error semantics, authorization, stale responses.
6. Dashboard/UI: all pages, widgets, charts, tables, labels, units, formatting,
   date ranges, timezone, refresh, loading/empty/error states, hardcoded/mock
   values, chart completeness, frontend state synchronization.
7. Reliability/security: background jobs, scheduler, queues, restarts, logging,
   monitoring, secret handling, dependency risks, access controls.
8. Tests: unit, integration, contract, regression, end-to-end, test data realism,
   coverage gaps, flaky tests, test isolation.

## Method
- Discover before assuming. Build an inventory of components and data flows.
- Read project requirements and identify ambiguous or conflicting specifications.
- Trace high-impact workflows end-to-end.
- Reproduce suspected defects safely where feasible.
- Compare implementation, runtime observations, persisted records, API output,
  and rendered UI.
- Independently recalculate high-impact metrics from source records when feasible.
- Record evidence and confidence; distinguish confirmed defect from hypothesis.
- Do not access production secrets or perform writes simply to inspect behavior.

## Finding format
Each finding must include:
- Stable ID (e.g. AUD-YYYYMMDD-001)
- Title and severity: CRITICAL / HIGH / MEDIUM / LOW / INFO
- Status: CONFIRMED / SUSPECTED / NOT_REPRODUCED / BLOCKED
- Affected component and workflow
- Expected versus actual behavior
- Reproduction steps and environment
- Evidence references (paths, line numbers, logs, query IDs, API captures)
- Root cause or "not yet established"
- Impact and likelihood
- Recommended correction
- Test/acceptance criteria
- Dependencies and safety concerns

## Required report
`AUDIT_REPORT.md` must contain:
1. Executive summary and audit boundary.
2. Architecture/component inventory.
3. Scope matrix (inspected, partially inspected, not inspected).
4. Trading logic and risk calculation findings.
5. Data pipeline and database findings.
6. Backend/API findings.
7. Dashboard and data reconciliation findings.
8. Reliability/security findings.
9. Tests executed with exact commands/results.
10. Defect register and root-cause analysis.
11. Prioritized remediation roadmap.
12. Limitations, assumptions, unresolved questions.

## Phase 1 exit criteria
- All mandatory scope areas are either inspected or explicitly marked not inspected
  with reasons.
- Findings have stable IDs and supporting evidence.
- High-impact data flows are mapped.
- No claim of complete coverage if important components remain inaccessible.
- Remediation plan is prioritized and testable.

Phase 1 does not authorize risky fixes. Move to Phase 2 only within user-granted
permissions.
