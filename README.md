# Universal Auto Trading Audit Skill for Antigravity

Version: 1.0.0

## What this is
A reusable Agent Skill that defines four workflows:
1. Full Project Audit
2. Controlled Remediation
3. Independent Verification
4. Continuous Audit

It includes mandatory loading instructions, checklists, quality gates, report
templates, JSON ledgers, and basic validation scripts.

## Install in Antigravity

### Project-level installation (recommended first)
1. Unzip this package.
2. Copy the folder `universal-auto-trading-audit` into the target project's
   `.agent/skills/` directory.
3. The expected layout is:

   ```
   your-project/
   ├── .agent/
   │   └── skills/
   │       └── universal-auto-trading-audit/
   │           ├── SKILL.md
   │           ├── references/
   │           ├── templates/
   │           └── scripts/
   └── ...
   ```

4. Open/reload the project in Antigravity and check that the Skill is discoverable
   in the Agent's Skills interface or skill listing.
5. If the installed Antigravity version uses a different skills directory or
   metadata convention, follow that version's documented convention. Do not
   assume the path silently worked; verify discovery.

### Global installation
If the goal is to use the Skill across all projects, use Antigravity's supported
global Skills directory for the installed version and copy the same folder there.
The global path can vary by version/platform; verify it in Antigravity's current
documentation or UI before installing. If uncertain, use project-level
installation first.

## Recommended mandatory project instruction
Add the following short rule to the project's always-loaded Agent instruction
file (for example `AGENTS.md` or the Antigravity-supported equivalent). Preserve
existing content; append rather than replace.

> For any task involving an automated trading bot's codebase, trading logic,
> data pipeline, database, API, dashboard, reliability, bug fixing, or release
> verification, load and follow the `universal-auto-trading-audit` Skill before
> substantive work. Read the applicable phase references, maintain an execution
> ledger, attach evidence to completed items, and enforce quality gates. If the
> Skill cannot be loaded, disclose this and do not claim compliance.

The Skill trigger description also supports automatic discovery, but explicit
project instructions improve reliability.

## First invocation
Ask the Agent:

> Load the `universal-auto-trading-audit` Skill. Run its preflight, inspect this
> repository and determine the appropriate phase. Do not modify code until you
> have established scope, permissions, baseline and a written plan. Initialize
> the audit ledger and report any missing references or blockers.

## Common invocations
- "Run a full Phase 1 audit of this trading bot."
- "Use Phase 2 to remediate the approved findings in AUDIT_REPORT.md."
- "Run an independent Phase 3 verification of the remediation."
- "Run Phase 4 continuous audit against the latest verified baseline."
- "Investigate this Dashboard/database mismatch using the Skill."

## Validation
From the Skill directory, run:

```bash
python scripts/validate_audit.py path/to/execution_ledger.json --findings path/to/finding_register.json
python scripts/validate_checklist.py path/to/checklist.json
python scripts/validate_phase_transition.py path/to/phase_status.json --to PHASE_2
```

These scripts perform structural checks only. They do not inspect the truth of
the evidence, prove code correctness, or replace human/independent review.

## Important limitations
- A Skill is an instruction package, not a hard security boundary or guaranteed
  workflow engine.
- Automatic activation and global discovery depend on Antigravity version and
  configuration. Verify the Skill is actually discoverable.
- For stronger enforcement, connect it to CI, repository policy, protected
  branches, test gates, permissions, and a separate QA agent.
- Never permit automatic live trading, production writes, destructive migrations,
  or deployment solely because a Skill says to do so.
