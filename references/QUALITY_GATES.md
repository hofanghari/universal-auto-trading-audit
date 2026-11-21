# Quality Gates

## Gate principles
- A phase gate is a decision rule, not a progress percentage.
- A failed mandatory criterion blocks phase acceptance.
- `NOT_TESTED`, `INCONCLUSIVE`, and `BLOCKED` are never equivalent to PASS.
- Exceptions require explicit user/authorized-owner approval, rationale, scope,
  mitigation, expiry/review date, and evidence. Never waive safety constraints.
- A percentage score must not conceal a failed Critical/High requirement.

## Gate 0 — Preflight
PASS only when Skill and relevant references are loaded, project context is
established, scope/permissions are known, and ledger is initialized.
Otherwise BLOCKED or NOT EVALUABLE.

## Gate 1 — Phase 1 audit
PASS only when scope coverage is honestly reported, key workflows are mapped,
findings have stable IDs and evidence, and uninspected areas are disclosed.
No unsupported "complete audit" claim.

## Gate 2 — Phase 2 remediation
PASS only when each assigned finding has an explicit outcome, changes are
traceable, tests are executed/reported, and unresolved work is carried forward.
This gate means remediation work is documented; it does not mean fixes are
independently accepted.

## Gate 3 — Phase 3 verification
ACCEPTED only when mandatory verification criteria pass and no unresolved
Critical/High defect remains. CONDITIONAL acceptance is only for approved,
documented non-critical risks. Otherwise REJECTED or NOT EVALUABLE.

## Gate 4 — Phase 4 continuous audit
PASS only when a valid baseline is identified, changes and impacted areas are
assessed, applicable checks are run, findings are updated, and evidence is saved.

## Phase transition
Before transition, validate:
1. Required report exists and is readable.
2. Required checklist items have statuses.
3. Completed items have evidence.
4. Blockers and exceptions are documented.
5. No prohibited status is silently treated as success.
6. Next phase's prerequisites are satisfied.

## Hard stops
Stop and request authorization before destructive database operations, production
writes, live deployments, strategy/risk changes, real-money execution, or
irreversible actions. Stop affected work if secrets or sensitive data may be
exposed, test isolation is compromised, or data integrity is at risk.
