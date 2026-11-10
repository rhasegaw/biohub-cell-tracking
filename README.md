# Biohub cell tracking: archival research release

Author: **Ryo Hasegawa**. This repository preserves a cleaned, source-backed Kaggle-style inference lineage for the Biohub - Cell Tracking During Development competition. It is an archival release, not a new benchmark run and not runnable by third parties without the omitted competition inputs and external artifacts.

## Result

The official Kaggle leaderboard records a Silver result at rank **51 of 3,947 teams** with private score **0.93486** (checked 2026-11-09):

- https://www.kaggle.com/competitions/biohub-cell-tracking-during-development
- https://www.kaggle.com/competitions/biohub-cell-tracking-during-development/leaderboard

The source record's preregistered rule recommended variants 201 and 244 as a final pair; the selection made in the Kaggle UI is not recorded locally. Variant 201 uses the corrected-detector lineage and variant 244 changes the declared ILP disappearance cost from `2` to `3.0`. The 244 source file as hashed fails its own configuration guard, so the archived 244 includes a one-line guard edit (expected disappearance `2` → `3.0`). Neither archived notebook is byte-mapped to the official scored submission.

## Method

The retained notebooks document the actual inference path:

1. `TemporalUNet3D` produces a 3D+t center heatmap; NMS and a sigmoid threshold produce point detections. A mandatory dual-seed low-margin consensus combines edge evidence at weight `0.20` and secondary detections at weight `0.80`.
2. `SimpleNodeTransformer` scores candidate adjacent-frame edges from contextual node features and relative coordinates. A `ForkHead` exists in the external support pack, but its contribution to the archived inference path was not verified.
3. An ILP selects an initial graph under one-parent/two-child constraints. Flow-based motion relinking using learned edge probabilities then replaces the ILP edge set in the archived configuration; final divisions therefore come mainly from post-link safe-division geometry, orphan-division recovery, and a 10-model mitosis-CNN ensemble.
4. The active configuration also includes position refinement at weight `0.5`, relink model override and low-probability pruning, bidirectional harmonic edge fusion at `0.15`, an 8-view TTA patch, and line-fit smoothing. The archived pair differs in the declared disappearance-cost guard; it is not a claim that the UI-selected submission used either exact archive byte sequence.

## Contents

- `notebooks/biohub-variant-201.ipynb`: cleared-output archival copy of the 201 lineage.
- `notebooks/biohub-variant-244.ipynb`: cleared-output archival copy of the 244 lineage.
- `metadata/variant-*.json`: source and archive SHA-256 hashes plus external-asset status.
- `research/results.md`: sourced results, balanced validation evidence, and limitations.
- `paper/paper.md`: technical report source; it is not peer-reviewed.
- `requirements.txt`: unpinned inventory from the notebook dependency table; versions of the scored run were not recorded; Python 3.12 is the archive metadata target.
- `scripts/smoke_test.py`: structural archive check; it does not run inference.
- `licenses/` and `NOTICE`: retained third-party license text and attribution boundary.

## External prerequisites and execution limits

The notebooks expect a Kaggle-style GPU environment, the competition input layout, and these public packs (not vendored here):

- Competition input: https://www.kaggle.com/competitions/biohub-cell-tracking-during-development
- DeepCenter center-prior pack: `biohub-deepcenter-unet3d-center-prior-v1` — https://www.kaggle.com/datasets/pilkwang/biohub-deepcenter-unet3d-center-prior-v1
- Temporal U-Net pack: `biohub-temporal-unet3d-seed314159-v1` — https://www.kaggle.com/datasets/pilkwang/biohub-temporal-unet3d-seed314159-v1
- Tracking support pack: `biohub-tracking-support-pack-50ep-v1` — https://www.kaggle.com/datasets/pilkwang/biohub-tracking-support-pack-50ep-v1

The default path additionally expects omitted, separately authorized artifacts:

- corrected detector `biohub-corrected-model-v1`, supplied through `BIOHUB_CORRECTED_MODEL_ROOT`;
- mitosis gate `biohub-mitosis-gate-jit288dorEN-v1`, containing `mitosis_cnn_all_fwd5_jit288dorEN_s0.pth` through `s9.pth`, with `BIOHUB_MITGATE=1`;
- `own_dense_refine.pt`, supplied through `BIOHUB_OWN_REFINE_PT`, with `BIOHUB_OWN_REFINE_W=0.5`.

Missing public packs, the corrected detector, DeepCenter weights, or mitosis-gate weights raise errors. Missing refinement weights leave positions unchanged; an 8-view TTA patch mismatch falls back to the default 4-way path; readmission and gap-filler failures are non-fatal; and missing candidate dumps can yield an empty candidate set. The corrected-detector artifact is located and hashed for display but is not checksum-verified, so a completed run is not evidence of the archived configuration. Internet-off execution was the intended mode when all wheels and assets were attached; it was not re-verified for this release. No inference, training, submission, or full replay was run while preparing this archive.

## Reproducibility boundary

The notebooks are cleaned publication copies: outputs, private authoring metadata, private dataset-owner slugs, and internal validator cells were removed. Source hashes in `metadata/variant-*.json` identify the original notebook bytes; archive hashes identify these modified publication copies. The exact official-submission mapping is unresolved, and omitted assets have not been redistributed. A future rerun must report its own asset hashes, notebook hash, environment, and official score separately from the result above.

## Links

- Portfolio: https://rhasegaw.github.io/
- Biohub case study: https://rhasegaw.github.io/work/biohub.html
- Technical report PDF: https://github.com/rhasegaw/biohub-cell-tracking/blob/main/paper/paper.pdf
- Kaggle profile: https://www.kaggle.com/ryohasegawa926

## License and attribution

This is a mixed-provenance archive. No license is granted for the author's own additions pending explicit publication approval. See `LICENSE`, `NOTICE`, and `THIRD_PARTY.md` for the Apache-2.0 base-notebook attribution, public dataset records, BSD-3-Clause baseline attribution, and redistribution boundary.
