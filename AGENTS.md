# AGENTS.md

## Purpose and Entry Points

`pte-prep` is the canonical local media and study-content workspace for PTE Academic preparation.

Read the root documents according to their role:

- [README.md](./README.md): learner entry point, stable directory index, and official resource links.
- [SOURCES.md](./SOURCES.md): canonical source allowlist, personal-study source list, promotion rules, and forbidden content.
- [STUDY_PLAN.md](./STUDY_PLAN.md): the current goal, diagnostic, learning priorities, daily schedule, and progress checkpoints.
- This file: the workspace contract for agents creating or maintaining guidance and reusable assets.

Keep each fact in its owning document. Link to the study plan instead of copying its schedule or priority table into other files. Read the relevant question-type guide only when working on that type.

Write learner explanations in Vietnamese. Keep filenames, metadata keys, question-type names, and English practice prompts/responses in English.

## Canonical Question-Type Order

The 22 numbered directories are indexed in README.md in Pearson's published question-type order. Preserve their existing names and numbering. Do not reorder or rename them without an explicitly authorized migration.

Learning order and learning priority belong in STUDY_PLAN.md; they do not change physical directory order. The unscored Personal Introduction can be covered by the study plan without adding a 23rd directory.

## Directory Contract

Each question-type directory uses:

```text
NN-question-type/
├── README.md
└── media/
    └── 001/
        ├── metadata.json
        └── <assets required by this item>
```

Create a per-type README or asset only when actually producing its content. An existing directory does not prove that its guide or dataset is ready. Do not create empty placeholder guides or unnecessary asset subdirectories.

Text-only types may contain text-only items. Do not attach audio, images, or video to a task that does not need them.

## Dataset Targets

Learning must start without waiting for a complete dataset. Use official practice resources through their authorized interfaces when local items are unavailable.

The workspace is endlessly extensible and is not constrained by any fixed-duration study plan. While a 7-day plan may exist as an optional strategy, the canonical dataset has no arbitrary limits on size, provided items meet quality, licensing, and provenance requirements.

As a structural baseline, an initial dataset configuration is illustrated below as **297 unique items**: **237 training + 30 Mock A + 30 Mock B**. This allocation is based on official item frequency, assessed skills, and partial-credit mechanics; it is an example starting point, not a strict cap.

| # | Question type | Total | Training | Mock A | Mock B |
| --- | --- | ---: | ---: | ---: | ---: |
| 01 | Read Aloud | 25 | 21 | 2 | 2 |
| 02 | Repeat Sentence | 40 | 32 | 4 | 4 |
| 03 | Describe Image | 10 | 8 | 1 | 1 |
| 04 | Retell Lecture | 8 | 6 | 1 | 1 |
| 05 | Answer Short Question | 8 | 6 | 1 | 1 |
| 06 | Summarize Group Discussion | 8 | 6 | 1 | 1 |
| 07 | Respond to a Situation | 8 | 6 | 1 | 1 |
| 08 | Summarize Written Text | 8 | 6 | 1 | 1 |
| 09 | Write Essay | 5 | 3 | 1 | 1 |
| 10 | Reading FIB — Dropdown | 28 | 24 | 2 | 2 |
| 11 | Reading MCMA | 4 | 2 | 1 | 1 |
| 12 | Reorder Paragraph | 12 | 10 | 1 | 1 |
| 13 | Reading FIB — Drag and Drop | 25 | 21 | 2 | 2 |
| 14 | Reading MCSA | 4 | 2 | 1 | 1 |
| 15 | Summarize Spoken Text | 7 | 5 | 1 | 1 |
| 16 | Listening MCMA | 4 | 2 | 1 | 1 |
| 17 | Listening FIB — Type In | 18 | 16 | 1 | 1 |
| 18 | Highlight Correct Summary | 4 | 2 | 1 | 1 |
| 19 | Listening MCSA | 4 | 2 | 1 | 1 |
| 20 | Select Missing Word | 4 | 2 | 1 | 1 |
| 21 | Highlight Incorrect Words | 18 | 16 | 1 | 1 |
| 22 | Write from Dictation | 45 | 39 | 3 | 3 |
|  | **Total** | **297** | **237** | **30** | **30** |

For each type, allocate stable IDs deterministically: the lowest IDs are `training`, the next IDs are `mock-a`, and the final IDs are `mock-b`. Do not reshuffle splits after a learner starts using either mock. Mock items must not appear in training, README worked examples, previews, or other learner-visible rehearsal paths before that mock is taken.

Maintain variety in speakers, topics, difficulty, and applicable image forms. Repeated attempts on one item are review attempts, not new items. Do not inflate counts to satisfy a target; quality, task fidelity, licensing, provenance, and transcript/answer correctness outrank count completion.

**Never fabricate canonical items to inflate counts.** Do not use LLM-authored questions, synthetic TTS, AI-generated images, placeholder charts, or invented prediction items in tracked `media/`. If no source-backed reviewed item is available, leave the slot empty and use authorized personal-study material under `private-materials/` instead.

Do not hardcode volatile current item counts in READMEs; derive current counts from the filesystem or existing tooling when requested. The table above is a target allocation, not a statement of current completion or exam readiness.

## Question-Type README Contract

Keep each guide usable during practice. Include only applicable sections:

1. Quick start and format: task steps, preparation/response timing, and relevant word limits.
2. Rules and scoring: assessed skills, official traits/raw score ranges, penalties, and zero-score conditions. Distinguish item scores from the reported 10–90 scale.
3. Prerequisite knowledge: only the grammar, vocabulary, pronunciation, listening, note-taking, or reasoning needed for this type.
4. Practice strategy for the current goal: explain the steps and trade-offs; link to STUDY_PLAN.md for priorities and daily scheduling.
5. Original worked examples: prompt, answer or illustrative response, and explanation of correct and incorrect choices. Clearly label text-only demonstrations of audio/image tasks.
6. Common mistakes, timed practice/correction/delayed retry, and a self-check checklist.
7. Local media notes: what an item must contain and how to use it.
8. Sources and date last verified.

Use one README per type by default. Split a substantial independently used supplement only when needed, with README as its entry point. Do not create separate rule/scoring/strategy files for all types. Link to shared knowledge rather than copying large lessons. Learner-facing guides must contain real explanations and examples, not empty section placeholders.

Use the current Pearson Score Guide for assessed skills and scoring rules, and Pearson format pages for interaction/timing. If official pages conflict, prefer the Score Guide for scoring and disclose the discrepancy rather than combining contradictory claims.

Label coaching choices as recommendations. Do not invent contribution percentages, guaranteed marks, official equivalences, or promises of reaching 40+ in seven days. Do not equate a homemade rubric or ChatGPT feedback with Pearson scores. Canonical dataset items must be source-backed; clearly labeled instructional examples in guides are not dataset items. Do not teach unrelated memorized answers or filler as a scoring technique.

## Media Item Contract

One `media/<item-id>/` directory represents one unique practice item. Use stable zero-padded local IDs such as `001`, `002`, and `003`; do not renumber existing items. Each item includes `metadata.json`.

Illustrative canonical metadata shape (schema example only, not a practice item):

```json
{
  "id": "example-001",
  "type": "<question-type-slug>",
  "difficulty": "medium",
  "split": "training",
  "review": {
    "content": "human-reviewed",
    "media": "human-reviewed"
  },
  "source": {
    "manifest_id": "<approved-id-from-SOURCES.md>",
    "provider": "<provider>",
    "url": "<traceable-asset-url>",
    "license": "<redistribution-license-or-explicit-permission>",
    "usage": "reusable",
    "attribution": "<required-attribution-or-null>",
    "retrieved_at": "YYYY-MM-DD"
  },
  "media": {
    "audio": "audio.mp3"
  },
  "content": {
    "transcript": "<verified-transcript>"
  },
  "answer": {
    "text": "<verified-answer>"
  }
}
```

Keep metadata simple, explicit, portable, and suitable for later application ingestion:

- `type` matches the directory slug without its numeric prefix; the ID is unique within that type.
- `split` is exactly `training`, `mock-a`, or `mock-b`; preserve it once assigned.
- Canonical items require `review.content: human-reviewed`. Use `review.media: human-reviewed` when media exists and `not-applicable` for text-only items. Machine validation alone never qualifies a canonical item.
- Canonical prompt, transcript, choices, and answer data live in metadata. Optional TXT sidecars are derived exports and must not be edited independently.
- Use only needed content/answer fields. Objective tasks require an answer key; open responses require scoring guidance and may have a clearly labeled illustrative response, never a single compulsory wording.
- Store media paths relative to the item directory. References must resolve to actual files; do not list absent or unused assets.
- Every canonical item needs `source.manifest_id` matching an approved canonical entry in `SOURCES.md`.
- External assets need a traceable URL or dataset identifier, license/permission evidence, applicable attribution, and retrieval date.
- A canonical item requires a traceable `source.url` or documented `source.dataset_id`; missing provenance is a hard failure.
- Difficulty is a curation judgment unless supported by an actual calibration; do not imply Pearson calibration.
- Generated/synthetic practice items are forbidden in canonical `media/`. Clearly labeled instructional examples may exist in README guides, but they are not dataset items.

## Source and Licensing Policy

Free access does not establish reuse rights. Record provider, provenance, license or permission, and relevant attribution for every reusable item.

Use `source.usage` to distinguish `reusable`, `reference-only`, and `unknown`. Only items with documented reusable rights belong in the reusable application dataset. Keep reference-only resources as links in documentation without copying their protected assets; unknown rights are not permission to ingest.

Do not scrape, mirror, redistribute, or ingest Pearson or commercial preparation assets into the reusable dataset unless their license or explicit permission allows the intended use. Study their format through permitted access. Canonical media must come from the source classes and promotion rules in [SOURCES.md](./SOURCES.md). Public-domain or clearly permissively licensed assets are eligible only after task-fidelity and human media review. Rights belong to the actual asset/version, not merely its provider's reputation.

### Local-only personal study materials

Third-party prediction books, PDFs, images, audio, and similar materials that the learner lawfully obtains for personal study may be stored under `private-materials/`. This area is intentionally excluded from Git except for its policy README and is not part of the canonical reusable dataset.

- Download only through provider-authorized access. Do not bypass paywalls, authentication, DRM, CAPTCHAs, or other access controls.
- Preserve the original provider/file naming when practical so the learner can identify the source later.
- Do not copy local-only third-party assets into numbered `media/` items, the application repository, releases, or other distributable locations unless reusable rights are separately documented.
- Do not treat prediction frequency, "high-frequency" labels, or sample answers from third-party material as Pearson scoring authority or a score guarantee.
- A local-only item may be useful for personal practice without being eligible for redistribution. Keep those two decisions separate.

## Quality and Format Defaults

Before accepting an item, check:

- Task behavior matches the intended format: prompt length, speaker count, timing, and response form where applicable.
- The asset opens; audio is intelligible and not clipped; images/text are readable.
- Machine checks can prove file integrity, parseability, references, and measurable timing; they do **not** prove that an image is exam-quality or that audio is intelligible/natural enough for practice.
- Transcript and answer match the actual asset. Audio must receive a real listening review and images a real visual review before `review.media` may become `human-reviewed`.
- Objective answers are correct and unambiguous; open-response examples are relevant.
- Provenance and usage rights are documented, with attribution where required.
- The item is traceable to an approved source, is not a mislabeled duplicate, and satisfies the promotion rules in `SOURCES.md`.

Prefer MP3 audio, WebP images, MP4 video only when needed, UTF-8 text, and JSON metadata. Preserve source quality where conversion would reduce usefulness. Exact format/timing verification belongs in the relevant guide, with a source and verification date.

## Scope and Completion

This workspace owns study guidance, the study plan, reusable assets, metadata, provenance, and dataset organization.

The PTE application repository owns runtime code, database schema, UI, scoring implementation, deployment, and product behavior. Keep this workspace data-oriented; do not introduce application infrastructure or modify the application as a side effect.

Preserve unrelated work and existing directories. Update only files needed by the current request. Verify Markdown links, JSON examples, ordering, and consistency after edits. Run `python3 tools/audit_sources.py` before claiming canonical media is valid. Report what changed and what content remains unavailable. Do not claim populated guides, licensed assets, score improvement, or PASS without evidence.
