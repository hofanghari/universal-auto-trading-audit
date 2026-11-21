# Universal Audit Checklist

Use only applicable items. Mark non-applicable items with a reason. Every
COMPLETED item requires evidence.

## A. Discovery and scope
- [ ] Confirm project root, environment and permissions.
- [ ] Read project instructions/specifications.
- [ ] Inventory services, modules, entry points and dependencies.
- [ ] Inventory DBs, schemas, APIs, workers, schedules and UI routes.
- [ ] Identify external data providers/exchanges and integrations.
- [ ] Map critical workflows and data lineage.
- [ ] Record inaccessible or out-of-scope areas.

## B. Trading logic
- [ ] Compare implementation with approved strategy/business specifications.
- [ ] Inspect signal generation, validation and deduplication.
- [ ] Inspect entry, exit, TP/SL and lifecycle transitions.
- [ ] Verify position sizing, leverage/margin and risk calculations as applicable.
- [ ] Verify fees, funding, spread and slippage treatment as applicable.
- [ ] Verify PnL, equity, balance, win rate, drawdown and other metric definitions.
- [ ] Check lookahead bias, leakage and candle/timeframe alignment where relevant.
- [ ] Check partial fills, rejected/cancelled orders and restart recovery.
- [ ] Verify paper/live boundaries and idempotency.

## C. Data and database
- [ ] Verify source, symbol mapping, precision and timestamp/timezone.
- [ ] Check stale, missing, duplicated, out-of-order and incomplete data.
- [ ] Inspect schema, constraints, indexes and migrations.
- [ ] Check transaction boundaries and concurrent writes.
- [ ] Reconcile events, orders, trades and persisted states.
- [ ] Check historical immutability and backup/recovery assumptions.

## D. Backend and integrations
- [ ] Inventory API endpoints and contracts.
- [ ] Compare API output with source records/database.
- [ ] Check validation, errors, pagination, filters and aggregation.
- [ ] Check caching and stale data.
- [ ] Check retry, timeout, reconnect and rate-limit behavior.
- [ ] Check auth boundaries and secret handling.

## E. Dashboard and UI
- [ ] Inventory pages, widgets, tables and charts.
- [ ] Trace each important display to API and source records.
- [ ] Independently recalculate critical metrics.
- [ ] Check labels, units, rounding, timezone and date ranges.
- [ ] Check hardcoded, mock, placeholder and stale values.
- [ ] Check chart completeness and zoom/pan/history loading.
- [ ] Check refresh, sorting, filters and pagination.
- [ ] Check loading, empty, unavailable and error states.
- [ ] Verify UI never reports success when underlying operation failed.

## F. Runtime and tests
- [ ] Inspect logs, exceptions and warnings.
- [ ] Check workers, scheduler, queues and duplicate execution.
- [ ] Check startup, shutdown, restart and recovery.
- [ ] Review tests and coverage gaps.
- [ ] Run relevant unit/integration/regression/E2E tests safely.
- [ ] Record exact commands, environment and results.

## G. Reporting and gates
- [ ] Assign stable Finding IDs and severity.
- [ ] Link evidence and acceptance criteria.
- [ ] Mark every checklist item with a valid status.
- [ ] Explain BLOCKED, NOT_APPLICABLE and NOT_TESTED items.
- [ ] Reconcile all remediation IDs through independent verification.
- [ ] Record gate outcome and unresolved risks.
