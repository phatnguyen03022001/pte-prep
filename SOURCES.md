# SOURCES.md

## Purpose

This file is the canonical source manifest for `pte-prep`.

It answers two separate questions:

1. **What sources are authoritative for PTE Academic rules, format, and scoring?**
2. **What sources may be used for personal practice or for reusable canonical assets?**

A source being useful for study does **not** automatically make its files eligible for GitHub redistribution.

Last verified: **2026-10-06**.

## Source classes

### A. Pearson official authority

Use Pearson as the authority for test structure, timing, scoring traits, official preparation, and official sample material.

| Source | Use | Canonical repo policy |
| --- | --- | --- |
| https://www.pearsonpte.com/pte-academic/preparation/ | Official preparation hub, Smart Prep, Scored Practice Tests, Official AI Practice | Use through authorized access. Do not mirror protected assets into Git unless redistribution rights are explicit. |
| https://www.pearsonpte.com/pte-academic/preparation/official-guide/ | Official Guide and official question bank | Official/authentic practice source. Keep downloaded/purchased material local-only unless Pearson explicitly permits redistribution. |
| https://www.pearsonpte.com/pte-academic/scoring/ | Current scoring information and Score Guide entry point | Authority for scoring facts. |
| https://www.pearsonpte.com/teachers/pte-academic-updates-partners-and-teachers/ | Official examples/resources for the newer speaking types | Use official downloads through Pearson. Treat downloads as local-only unless redistribution permission is explicit. |

Pearson wins over third-party coaching sources when scoring, timing, skills assessed, or task behavior conflicts.

### B. Third-party personal-study sources

These sources may be useful for prediction banks or additional practice variety. They are **not Pearson authority**.

| Provider | Verified entry point | Intended use | Git policy |
| --- | --- | --- | --- |
| ApeUni | https://www.apeuni.com/blog/mobile/how_to_download_pte_prediction_en?locale=en | Provider-authorized study-material downloads / prediction material | Store under `private-materials/apeuni/`; never commit downloaded assets without separate reuse permission. |
| PTE Nepal | https://ptenepal.com/blog/pte-prediction-oct5-11-2026-describe-image/ | Weekly prediction material and Describe Image practice | Store under `private-materials/pte-nepal/`; never mirror assets into canonical `media/` without explicit reusable rights. |

Prediction, recall, “high-frequency”, or forecast labels are coaching signals only. They are not official Pearson frequency data and do not guarantee exam appearance.

### C. Reusable canonical media sources

#### Approved canonical source registry

| `manifest_id` | Provider/source | Scope | Redistribution evidence | Status |
| --- | --- | --- | --- | --- |
| _none_ | — | — | — | **No canonical media source is currently approved.** |

Until this registry contains an approved `manifest_id`, tracked `NN-question-type/media/` must remain empty. Adding a source requires an intentional update to this file with asset-level rights evidence; usefulness for study is not enough.

A file may enter a tracked `NN-question-type/media/` directory only when **all** of the following are true:

- `source.manifest_id` exactly matches an approved entry in the registry above;
- the exact asset has a traceable source URL or dataset identifier;
- the exact asset has documented redistribution/reuse rights;
- required attribution is recorded;
- the content has been manually checked for task fidelity;
- any audio has been listened to by a human reviewer;
- any image has been visually reviewed by a human reviewer;
- the item is not copied from a protected prediction bank, commercial prep bank, or Pearson resource without explicit redistribution permission;
- `python3 tools/audit_sources.py` passes.

Acceptable examples include asset-level public-domain material, clearly compatible Creative Commons material, or material with explicit written permission for repository redistribution.

## Forbidden canonical content

The following are **not allowed** in tracked canonical `media/`:

- ChatGPT/LLM-generated practice questions used merely to fill a quota;
- synthetic TTS audio;
- AI-generated images;
- placeholder/wireframe charts or diagrams;
- invented “prediction” questions;
- unknown-provenance downloads;
- screenshots or copied commercial/Pearson assets without redistribution rights;
- items that have only machine validation but no human content/media review;
- low-quality assets kept only to satisfy the 297-item target.

The 297-item table in `AGENTS.md` is a **target allocation**, never permission to fabricate content.

## Local-only personal material layout

Downloaded personal-study material belongs here:

```text
private-materials/
├── README.md
├── apeuni/
│   └── <YYYY-MM>/
└── pte-nepal/
    └── <YYYY-MM-DD>/
```

Everything below `private-materials/` except its README is ignored by Git.

## Promotion rule

A local third-party file is **not promoted** into canonical `media/` simply because it is useful.

Promotion requires a separate rights check, provenance record, task-fidelity review, and human media review. If any one of those is missing, keep it local-only.
