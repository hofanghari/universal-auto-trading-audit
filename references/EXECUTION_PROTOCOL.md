# Execution Protocol and State Management

## Recommended project storage
Create an audit workspace in the target repository, for example:
`audit/runs/<RUN_ID>/` with:
- `execution_ledger.json`
- `finding_register.json`
- `phase_status.json`
- phase reports and evidence index.

Do not overwrite completed runs. Use a unique run ID (UTC timestamp plus short
identifier) and preserve history. Do not store secrets, raw account credentials,
or unnecessary personal/financial data in audit artifacts.

## Status vocabulary
Checklist: NOT_STARTED, IN_PROGRESS, COMPLETED, BLOCKED, NOT_APPLICABLE,
NOT_TESTED, INCONCLUSIVE.
Finding: CONFIRMED, SUSPECTED, NOT_REPRODUCED, BLOCKED, RESOLVED_PENDING_VERIFICATION,
PARTIALLY_RESOLVED, VERIFIED_FIXED, FAILED, NOT_TESTED, INCONCLUSIVE.
Gate: PASS, FAIL, BLOCKED, NOT_EVALUABLE.

## Ledger discipline
- Create an item before doing the work.
- Update status when work starts, ends, or is blocked.
- Evidence references must resolve to an artifact or reproducible observation.
- Record command, timestamp, environment and result for tests.
- Never put credentials or private keys in evidence.
- If execution is interrupted, resume from ledger; re-check environment and
  current worktree before continuing.
- Revalidate prior completed items if relevant code/data changed after their
  evidence was collected.

## Scope control
Use a risk-based, change-based test plan. Do not claim every file was manually
reviewed if only automated scanning was performed. Separate automated scans,
manual inspection and runtime validation in reports.

## Agent handoff
A handoff must include run ID, phase, completed items, pending items, blockers,
finding IDs, evidence paths, environment assumptions and next safe action.
