#!/usr/bin/env python3
"""Validate the structured Awesome Strategy Skills catalog."""

from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "catalog.json"
README_PATH = ROOT / "README.md"

REQUIRED_FIELDS = {
    "id",
    "name",
    "url",
    "publisher",
    "kind",
    "category",
    "status",
    "license",
    "last_reviewed",
    "description",
    "why_included",
    "conflict",
}

KINDS = {"skill", "collection"}
STATUSES = {"petrichor-original", "reviewed", "collection"}
CATEGORIES = {
    "customer-market-intelligence",
    "positioning-competitive",
    "product-portfolio",
    "go-to-market-growth",
    "pricing-monetization",
    "executive-decisions",
    "measurement-experimentation",
    "execution-systems",
    "collections-discovery",
}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"catalog: unable to load {CATALOG_PATH}: {exc}", file=sys.stderr)
        return 1

    try:
        readme = README_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"catalog: unable to load {README_PATH}: {exc}", file=sys.stderr)
        return 1

    if catalog.get("schema_version") != "1.0.0":
        fail(errors, "catalog: schema_version must be 1.0.0")

    entries = catalog.get("entries")
    if not isinstance(entries, list) or not entries:
        fail(errors, "catalog: entries must be a non-empty list")
        entries = []

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    today = date.today()
    stale_before = today - timedelta(days=180)

    for index, entry in enumerate(entries):
        label = f"entry[{index}]"
        if not isinstance(entry, dict):
            fail(errors, f"{label}: must be an object")
            continue

        missing = REQUIRED_FIELDS - entry.keys()
        if missing:
            fail(errors, f"{label}: missing fields: {', '.join(sorted(missing))}")
            continue

        entry_id = entry["id"]
        label = f"entry[{index}] {entry_id!r}"

        if not isinstance(entry_id, str) or not ID_PATTERN.fullmatch(entry_id):
            fail(errors, f"{label}: id must be a lowercase hyphenated slug")
        elif entry_id in seen_ids:
            fail(errors, f"{label}: duplicate id")
        seen_ids.add(entry_id)

        url = entry["url"]
        parsed = urlparse(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != "https" or not parsed.netloc:
            fail(errors, f"{label}: url must be an absolute HTTPS URL")
        elif url in seen_urls:
            fail(errors, f"{label}: duplicate url")
        seen_urls.add(url)

        if url not in readme:
            fail(errors, f"{label}: canonical url does not appear in README.md")

        if entry["kind"] not in KINDS:
            fail(errors, f"{label}: invalid kind {entry['kind']!r}")
        if entry["status"] not in STATUSES:
            fail(errors, f"{label}: invalid status {entry['status']!r}")
        if entry["category"] not in CATEGORIES:
            fail(errors, f"{label}: invalid category {entry['category']!r}")

        if entry["status"] == "collection" and entry["kind"] != "collection":
            fail(errors, f"{label}: collection status requires collection kind")
        if entry["status"] == "petrichor-original" and entry["conflict"] == "none":
            fail(errors, f"{label}: Petrichor originals require a conflict disclosure")

        for field in ("name", "publisher", "license", "description", "why_included", "conflict"):
            if not isinstance(entry[field], str) or not entry[field].strip():
                fail(errors, f"{label}: {field} must be a non-empty string")

        if isinstance(entry["description"], str) and not entry["description"].endswith("."):
            fail(errors, f"{label}: description must end with a period")
        if isinstance(entry["why_included"], str) and not entry["why_included"].endswith("."):
            fail(errors, f"{label}: why_included must end with a period")

        try:
            reviewed = datetime.strptime(entry["last_reviewed"], "%Y-%m-%d").date()
        except (TypeError, ValueError):
            fail(errors, f"{label}: last_reviewed must use YYYY-MM-DD")
        else:
            if reviewed > today:
                fail(errors, f"{label}: last_reviewed cannot be in the future")
            if reviewed < stale_before:
                fail(errors, f"{label}: review is older than 180 days")

    if len(entries) < 25:
        fail(errors, "catalog: initial release must contain at least 25 editorial entries")

    if errors:
        print("Catalog validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Catalog valid: {len(entries)} entries, {len(CATEGORIES)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

