# Report Templates

Copy only the template(s) relevant to the active phase. Replace placeholders;
never leave invented values.

## AUDIT_REPORT.md
# Full Project Audit
- Run ID:
- Date/time (UTC):
- Project/revision:
- Environment:
- Auditor(s):
- Scope and exclusions:
- References loaded:
- Executive summary:
- Architecture/component inventory:
- Data-flow maps:
- Findings by severity:
- Finding register location:
- Database/data pipeline:
- Trading logic/calculation:
- API/backend:
- Dashboard/UI reconciliation:
- Runtime/security/reliability:
- Tests actually executed:
- Coverage limitations:
- Remediation priorities:
- Gate result:

## REMEDIATION_REPORT.md
# Controlled Remediation Report
- Run ID:
- Source audit run:
- Revision before/after:
- Environment:
- Authorized scope:
- Finding ID | Status | Root cause | Changes | Tests | Evidence:
- Regression results:
- Blocked/not tested:
- Rollback notes:
- Remaining risks:
- Gate result:

## VERIFICATION_REPORT.md
# Independent Verification Report
- Run ID:
- Source audit/remediation run:
- Verifier and independence statement:
- Revision verified:
- Environment:
- Finding ID | Verification status | Test | Evidence | Notes:
- DB/API/dashboard reconciliation:
- Regression/edge cases:
- New findings:
- Limitations:
- Release recommendation:
- Gate result:

## CONTINUOUS_AUDIT_REPORT.md
# Continuous Audit Report
- Run ID and audit window:
- Verified baseline:
- Current revision/config/schema:
- Changes since baseline:
- Impact analysis:
- Checks and results:
- New findings:
- Regressions/recurrences:
- Data/dashboard consistency:
- Reliability trends:
- Outstanding risks/actions:
- Gate result:

## Finding register entry
{
  "finding_id": "AUD-YYYYMMDD-001",
  "title": "Short factual title",
  "severity": "HIGH",
  "status": "CONFIRMED",
  "component": "module/service/page",
  "expected": "Expected behavior",
  "actual": "Observed behavior",
  "evidence": ["path:line or test/log/query reference"],
  "root_cause": "Established cause or not yet established",
  "impact": "Observed or plausible impact",
  "acceptance_criteria": ["verifiable criterion"],
  "remediation_status": "NOT_STARTED",
  "verification_status": "NOT_TESTED"
}
