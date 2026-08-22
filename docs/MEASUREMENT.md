# Measurement Plan

Awesome Strategy Skills is a marketing asset only if it creates measurable trust and qualified movement toward Petrichor. The measurement system separates attention, utility, authority, and commercial intent.

## Decisions this data informs

| Question | Decision |
|---|---|
| Which sources bring qualified readers? | Where Petrichor should invest distribution time. |
| Which categories and assets earn the most engagement? | What to evaluate, expand, or turn into research. |
| Do readers move from the catalog to Resilience Stack? | Whether the editorial-to-product path is clear. |
| Do Resilience Stack visitors start and complete diagnostics? | Whether the offer and routing match audience intent. |
| Which contributors create backlinks and referrals? | Where the community flywheel is working. |

## Funnel

| Stage | Primary measures | Interpretation |
|---|---|---|
| Discovery | Repository unique views, referral sources, landing-page sessions | The asset is being found. |
| Utility | Clone uniques, stars, forks, returning visitors, catalog interactions | The asset is useful enough to retain or reuse. |
| Authority | Backlinks, citations, contributor nominations, independent reviewers | Other people are willing to attach their reputation to it. |
| Product interest | Resilience Stack sessions, diagnostic CTA clicks, GitHub-to-site rate | Editorial trust is transferring to Petrichor IP. |
| Commercial intent | Diagnostic completions, qualified contact submissions, strategy calls | The asset is creating relevant demand. |

## GitHub measures

GitHub traffic data is retained for a limited window, so the `Traffic Snapshot` workflow captures a weekly artifact.

The traffic endpoints reject the built-in Actions token. To enable snapshots, add a repository administrator token that can read GitHub traffic endpoints as the Actions secret `TRAFFIC_TOKEN`. Until it is configured, the workflow exits successfully and records an explicit skip in the run summary.

| Measure | Source | Cadence |
|---|---|---|
| Views and unique visitors | GitHub Traffic API | Weekly. |
| Clones and unique cloners | GitHub Traffic API | Weekly. |
| Top referrers and paths | GitHub Traffic API | Weekly. |
| Stars, forks, watchers, issues | GitHub Repository API | Weekly. |
| Nominations and accepted entries | GitHub issues and pull requests | Monthly editorial review. |

## Website events

Use object-action names and keep campaign details in properties.

| Event | Trigger | Properties | Decision supported |
|---|---|---|---|
| `strategy_catalog_viewed` | Companion landing page loads | `page_path`, `utm_source`, `utm_medium`, `utm_campaign` | Distribution quality. |
| `strategy_catalog_clicked` | Visitor opens the GitHub catalog | `cta_location`, `destination`, campaign properties | Landing-page utility. |
| `resilience_stack_clicked` | Visitor opens Resilience Stack from the companion page | `cta_location`, `destination`, campaign properties | Editorial-to-product transfer. |
| `diagnostic_started` | Visitor opens a Tally diagnostic | `diagnostic_name`, `cta_location`, campaign properties | Diagnostic demand. |
| `strategy_contact_clicked` | Visitor opens the Petrichor contact path | `cta_location`, campaign properties | Commercial intent. |

Do not send names, email addresses, free-text responses, company names, or other PII as analytics properties.

## UTM convention

Canonical repository-to-site links use:

```text
utm_source=github
utm_medium=referral
utm_campaign=awesome-strategy-skills
utm_content=<placement>
```

Launch distribution should preserve the campaign and vary source, medium, and content:

| Channel | Source | Medium | Example content |
|---|---|---|---|
| Philipp LinkedIn | `linkedin` | `social` | `founder_launch` |
| Petrichor LinkedIn | `linkedin` | `social` | `company_launch` |
| Newsletter | `newsletter` | `email` | `launch_issue` |
| Contributor outreach | `contributor_outreach` | `email` | `listed_author` |
| Hacker News | `hacker_news` | `community` | `show_hn` |

## Launch baseline

The initial baseline is recorded in [`data/metrics/baseline-2026-08-22.json`](../data/metrics/baseline-2026-08-22.json). The repository was intentionally measured before public distribution so later lift is interpretable.

## Review rhythm

- **Weekly:** Traffic, link health, stars, clones, and new nominations.
- **Monthly:** Referral quality, Resilience Stack click-through, diagnostic starts, and accepted contributions.
- **Quarterly:** Backlinks, citations, independent reviews, qualified inquiries, and the State of AI Strategy Skills report.

Success is not the largest possible star count. It is a growing ratio of qualified use, credible third-party participation, and measurable movement into Petrichor's diagnostic and consulting paths.
