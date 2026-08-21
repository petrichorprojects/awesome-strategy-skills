# Security Policy

## What this repository does

This repository links to third-party agent skills. It does not vendor or execute those skills. Inclusion is an editorial review, not a security audit or warranty.

Agent skills may contain instructions or scripts capable of reading files, changing systems, accessing networks, calling APIs, or sending data to external services.

## Safe evaluation

Before installing a listed skill:

1. Read the full skill file and every referenced script, template, hook, and dependency.
2. Check permissions, environment variables, filesystem access, network calls, and external tool requirements.
3. Look for prompt-injection exposure when the workflow processes web pages, documents, messages, or other untrusted content.
4. Test with synthetic data in a sandbox, container, virtual machine, or disposable project.
5. Pin a known commit or release for production use.
6. Keep secrets out of prompts, logs, fixtures, and generated artifacts.
7. Require human approval for destructive actions, payments, publishing, external messages, or consequential business decisions.

## Reporting

Use GitHub's private vulnerability reporting for vulnerabilities in this repository's automation or files. For a vulnerability in a linked project, report it to that project's maintainers first.

For an unsafe, malicious, compromised, or misleading listed resource, open a public issue only if doing so will not expose an unpatched exploit. Otherwise contact Petrichor Projects through the security contact published at [petrichorgrowth.com](https://petrichorgrowth.com).

We may remove or quarantine a link while a report is investigated.

