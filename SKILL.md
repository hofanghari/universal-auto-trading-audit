---
name: universal-auto-trading-audit
description: >
  Use when auditing, debugging, repairing, verifying, or continuously monitoring
  an automated trading bot or trading platform. Covers codebase, trading logic,
  data pipelines, databases, APIs, dashboards, execution integrity, remediation,
  independent verification, and regression monitoring. Activate for full audits,
  defect investigations, dashboard/data discrepancies, post-change checks, and
  requests to improve reliability or correctness of an auto-trading system.
---

# Universal Auto Trading Audit

## Mission
Apply a repeatable, evidence-driven audit and quality-control process to automated
trading software. The objective is to establish whether actual system events,
persisted records, calculations, APIs, and dashboard reports agree.

This Skill is a methodology and execution protocol, not proof that the platform
has enforced every instruction. Follow it, keep durable records, and disclose
platform or permission limitations.

## Mandatory entry protocol
Before substantive work on a relevant task:

1. Read this entire `SKILL.md`.
2. Identify the task type and applicable phase(s).
3. Read the corresponding reference file(s) in `references/`.
4. Inspect project instructions and architecture (for example `AGENTS.md`,
   `GEMINI.md`, `CLAUDE.md`, README, runbooks, CI configuration). Do not overwrite
   existing instructions; propose a minimal additive integration if needed.
5. Establish the working directory, environment, permissions, and whether this
   is development, staging, paper trading, or production.
6. Initialize or update the execution ledger using `templates/`.
7. State the intended scope, non-goals, safety boundaries, and validation plan.
8. Execute in small, traceable units. Record evidence as work progresses.

If a required reference file is missing or unreadable, stop the affected workflow,
report the gap, and do not pretend the Skill was fully loaded.

## Task routing
- New project, broad health review, or "audit everything": Phase 1.
- Fixing findings from an audit: Phase 2.
- Confirming fixes or release readiness: Phase 3.
- After code/config/schema/strategy/integration changes, or recurring health checks: Phase 4.
- If the request spans multiple phases, execute them in order and enforce each gate.
- For a single narrow defect, use a scoped Phase 1 investigation, Phase 2 remediation,
  and Phase 3 verification. Do not run unrelated checks merely to inflate scope.
- If intent or authority is unclear for a destructive or production action, ask first.

## Four-phase lifecycle
1. **Full Project Audit** — inspect and produce an evidence-backed defect register.
   Read `references/PHASE_1_FULL_AUDIT.md`.
2. **Controlled Remediation** — repair authorized defects in small batches.
   Read `references/PHASE_2_REMEDIATION.md`.
3. **Independent Verification** — independently verify every fix and acceptance
   criterion; the implementer cannot self-approve its own work.
   Read `references/PHASE_3_VERIFICATION.md`.
4. **Continuous Audit** — compare changes against a verified baseline and detect
   regression/new risks. Read `references/PHASE_4_CONTINUOUS_AUDIT.md`.

Read `references/AUDIT_CHECKLIST.md`, `references/QUALITY_GATES.md`,
`references/EXECUTION_PROTOCOL.md`, and `references/REPORT_TEMPLATES.md` whenever
the corresponding workflow is active.

## Non-negotiable rules
- Evidence over assertions. "Code exists" is not proof that a feature works.
- No evidence means NOT VERIFIED, not COMPLETED.
- Distinguish VERIFIED PASS, VERIFIED FAIL, NOT TESTED, BLOCKED, and INCONCLUSIVE.
- Never invent test results, logs, database rows, API responses, screenshots, or metrics.
- Never hide a failed test or downgrade severity without a documented reason.
- Do not change trading strategy rules, thresholds, indicators, filters, or risk
  parameters unless explicitly authorized.
- Never place live orders or cause real-money trading as part of audit/testing.
- Never alter balances, trade history, fills, PnL, or equity to make reports match.
- Never delete or rewrite historical records to conceal discrepancies.
- Do not expose credentials, tokens, private keys, or sensitive account data.
- Do not run destructive migrations, production deployments, data cleanup, or
  irreversible commands without explicit authorization and a rollback plan.
- Use read-only inspection first. Prefer isolated test fixtures and staging.
- Keep paper-trading and live-trading boundaries explicit.
- Preserve existing project conventions and avoid unrelated rewrites.

## Data-to-dashboard invariant
For every material metric or status, trace:

Actual event/source -> ingestion -> validation/normalization -> business logic /
calculation -> database persistence -> API -> frontend state -> displayed value.

Independently recalculate critical metrics from source records where feasible.
Check definitions, time windows, timezone, rounding, fees, slippage, status filters,
partial fills, closed/open trade treatment, and duplicate handling. A displayed
value is trustworthy only when its lineage and reconciliation are demonstrated.

## Execution ledger and evidence
Use `templates/execution_ledger.json` as a schema/example and maintain a project-
specific copy in a durable project location (recommended:
`audit/active/execution_ledger.json`). Also maintain a finding register and phase
status file. Do not overwrite historical audit runs; archive each completed run
with a timestamp or unique run ID.

Each checklist item must have a status:
`NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `BLOCKED`, `NOT_APPLICABLE`,
`NOT_TESTED`, or `INCONCLUSIVE`.

Every `COMPLETED` item must cite evidence (file/line, command and result, test ID,
query and summarized output, API response capture, screenshot reference, or
reproducible observation). `NOT_APPLICABLE` requires a reason. Blocked work needs
a blocker and owner/next action. Do not use a checkbox alone as proof.

## Quality gates
Apply `references/QUALITY_GATES.md`. A failed gate blocks dependent phase
acceptance. The Director/lead agent must not override a failed gate merely to
produce a successful report. Record any explicitly authorized exception, its
approver, rationale, risk, and expiry.

## Multi-agent operation
When available, separate roles:
- Audit Agent: discovery and defect identification.
- Engineering Agent: implementation of authorized fixes.
- QA Agent: independent verification.
- Data Auditor: source/database/API/dashboard reconciliation.
- Director: scope, sequencing, permissions, conflict resolution, and gates.

The Engineering Agent must not independently mark its own fix VERIFIED FIXED.
If only one agent is available, clearly disclose the lack of independent review
and classify the result accordingly.

## Required outputs
Create/update reports appropriate to the phase:
- `AUDIT_REPORT.md`
- `REMEDIATION_REPORT.md`
- `VERIFICATION_REPORT.md`
- `CONTINUOUS_AUDIT_REPORT.md`

Maintain stable Finding IDs and cross-reference each finding through remediation
and verification. Use `references/REPORT_TEMPLATES.md`.

## Completion statement
At the end, report:
- phase(s) run and scope actually covered;
- references loaded;
- completed / blocked / not tested / inconclusive checklist counts;
- findings by severity and status;
- tests actually executed and results;
- evidence locations;
- unresolved risks and required approvals;
- gate result: PASS, FAIL, or NOT EVALUABLE.

Never state "full audit complete", "fixed", or "accepted" when coverage or evidence
does not support that claim.
