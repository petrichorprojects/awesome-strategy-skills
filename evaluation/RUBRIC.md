# Petrichor Strategy Skill Index

The Petrichor Strategy Skill Index is a review framework for asking a practical question:

> Does this skill improve the quality, traceability, and resilience of a consequential decision?

It is not a popularity ranking. Stars, forks, prose volume, and model fluency are excluded from the score.

## Scoring model

Each dimension is scored from 0 to 3. The maximum score is 24.

| Score | Meaning |
|---|---|
| 0 | Missing or actively harmful. |
| 1 | Mentioned but underspecified, inconsistent, or easy to bypass. |
| 2 | Operational and useful with identifiable limitations. |
| 3 | Explicit, testable, robust, and integrated throughout the workflow. |

### 1. Decision specificity

- **0:** Produces generic advice or content without a defined decision.
- **1:** Names a topic but leaves the decision and owner unclear.
- **2:** Defines the decision, audience, and expected output.
- **3:** Defines the decision, owner, timing, alternatives, and commitment boundary.

### 2. Evidence discipline

- **0:** Invents or implies facts, research, or certainty.
- **1:** Requests context but does not distinguish evidence from assumption.
- **2:** Requires relevant inputs and labels gaps or inference.
- **3:** Preserves provenance, tests evidence quality, and refuses unsupported conclusions.

### 3. Workflow integrity

- **0:** A loose prompt or persona with no process.
- **1:** A checklist without clear activation, order, or completion.
- **2:** A bounded sequence with prerequisites and deliverables.
- **3:** A resumable or auditable workflow with gates, state, and explicit completion criteria.

### 4. Trade-off quality

- **0:** Recommends one answer without alternatives or costs.
- **1:** Mentions pros and cons generically.
- **2:** Compares viable alternatives against relevant criteria.
- **3:** Makes opportunity cost, reversibility, second-order effects, and ownership explicit.

### 5. Adversarial resilience

- **0:** Confirms the user's preferred story.
- **1:** Includes generic caveats.
- **2:** Tests counterarguments, failure modes, or downside scenarios.
- **3:** Uses structured cross-examination, pre-mortems, red teams, or disconfirming evidence.

### 6. Output utility

- **0:** Produces inspiration with no usable artifact.
- **1:** Produces a summary that requires substantial reconstruction.
- **2:** Produces a concrete artifact with decisions, rationale, and next actions.
- **3:** Produces audience-ready artifacts plus traceable evidence, owners, and review triggers.

### 7. Safety and human ownership

- **0:** Encourages unsafe autonomy, hidden actions, or false certainty.
- **1:** Includes broad disclaimers without operational controls.
- **2:** Defines meaningful limitations, approvals, and sensitive-data boundaries.
- **3:** Applies least privilege, untrusted-input handling, escalation, and human decision ownership throughout.

### 8. Reproducibility and maintenance

- **0:** No source, license, version, or stable instructions.
- **1:** Source exists but provenance or maintenance is unclear.
- **2:** Versioned source, usable license, and repeatable instructions are present.
- **3:** Tests or evaluations, changelog, clear ownership, versioned dependencies, and active maintenance are present.

## Interpretation

| Total | Interpretation |
|---|---|
| 0–8 | Prompt-shaped content; not suitable for consequential strategy work. |
| 9–14 | Useful scaffold with significant operator burden. |
| 15–19 | Decision-supporting skill with identifiable limitations. |
| 20–24 | Strong candidate for high-consequence work with appropriate human ownership. |

A total score never overrides a critical failure. Fabricated evidence, malicious behavior, deceptive provenance, missing license, or unsafe external action can disqualify a skill regardless of total.

## Evaluation protocol

1. Pin the exact commit or release being evaluated.
2. Record evaluator identity and any relationship to the project.
3. Use the same task fixture for comparable skills.
4. Preserve inputs, outputs, tool traces where safe, and evaluator notes.
5. Score each dimension with direct evidence.
6. Have a second reviewer independently score high-visibility comparisons.
7. Resolve disagreements by discussing evidence, not averaging opinions invisibly.
8. Publish material limitations and critical failures alongside the score.

Use [template.md](template.md) for evaluation records.

## Current maturity

Version 0.1 defines the rubric and evidence format. The catalog does not yet publish empirical scores for every entry. Scores will be added only when the pinned source, fixture, output, and review record are public enough to audit.

