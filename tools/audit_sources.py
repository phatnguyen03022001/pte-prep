#!/usr/bin/env python3
"""Fail if tracked canonical media violates the pte-prep source gate."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPROVED_CANONICAL_SOURCE_IDS: set[str] = set()

FORBIDDEN_PROVIDERS = {
    "original-authoring+piper-tts",
    "synthetic",
    "ai-generated",
    "llm-generated",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)


def main() -> int:
    errors = 0
    items = sorted(ROOT.glob("[0-9][0-9]-*/media/*/metadata.json"))

    for metadata_path in items:
        try:
            data = json.loads(metadata_path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{metadata_path.relative_to(ROOT)}: invalid JSON: {exc}")
            errors += 1
            continue

        rel = metadata_path.relative_to(ROOT)
        source = data.get("source") or {}
        review = data.get("review") or {}
        generation = data.get("generation") or {}
        media = data.get("media") or {}

        provider = str(source.get("provider") or "").strip()
        provider_lower = provider.lower()
        manifest_id = str(source.get("manifest_id") or "").strip()

        if manifest_id not in APPROVED_CANONICAL_SOURCE_IDS:
            fail(f"{rel}: source.manifest_id {manifest_id!r} is not approved in SOURCES.md")
            errors += 1

        if provider_lower in FORBIDDEN_PROVIDERS or "piper" in provider_lower:
            fail(f"{rel}: forbidden generated/synthetic provider {provider!r}")
            errors += 1

        if generation.get("synthetic") is True:
            fail(f"{rel}: synthetic generation is forbidden in canonical media")
            errors += 1

        if source.get("usage") != "reusable":
            fail(f"{rel}: source.usage must be 'reusable'")
            errors += 1

        if not source.get("license"):
            fail(f"{rel}: source.license is required")
            errors += 1

        if not (source.get("url") or source.get("dataset_id")):
            fail(f"{rel}: traceable source.url or source.dataset_id is required")
            errors += 1

        if review.get("content") != "human-reviewed":
            fail(f"{rel}: review.content must be 'human-reviewed'")
            errors += 1

        expected_media_review = "human-reviewed" if media else "not-applicable"
        if review.get("media") != expected_media_review:
            fail(
                f"{rel}: review.media must be {expected_media_review!r}, "
                f"got {review.get('media')!r}"
            )
            errors += 1

        for kind, asset_rel in media.items():
            asset = metadata_path.parent / str(asset_rel)
            if not asset.is_file() or asset.stat().st_size == 0:
                fail(f"{rel}: missing/empty {kind} asset {asset_rel!r}")
                errors += 1

    if errors:
        print(f"SOURCE_GATE_FAIL items={len(items)} errors={errors}", file=sys.stderr)
        return 1

    print(f"SOURCE_GATE_PASS canonical_items={len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
