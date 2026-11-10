# A structured inference pipeline for 3D+t zebrafish cell tracking

**Ryo Hasegawa**

**Technical report — archival release, checked 2026-11-09; not peer-reviewed**

## Abstract

This report describes an archival inference pipeline for the Biohub - Cell Tracking During Development task. The system detects nuclei in 3D+t fluorescence volumes and links them into a graph containing cell divisions. It combines a temporal 3D U-Net detector, a context-aware transformer edge scorer, initial integer-linear-programming (ILP) graph selection, flow-based motion relinking, and conservative post-link division checks. The official Kaggle record reports rank 51 of 3,947 teams with a Silver medal and private score 0.93486. That externally judged outcome is separated from source-record validation evidence. Neither archived variant is byte-mapped to the official scored submission; external weights and data are omitted, and the retained held-out evidence does not establish a confidence-separated gain for either archived variant as a whole.

## 1. Problem and data

Each sample is a short 3D+t microscopy movie of fluorescently labeled zebrafish embryo cells. The inference output is a table of detections and temporal edges, including division edges. The competition metric is:

\[
S = \mathrm{adjusted\_edge\_jaccard} + 0.1\,\mathrm{division\_jaccard},
\]

with a 7 µm bipartite match for node identity. The official scorer and competition description are listed in the references.

## 2. Methods

### 2.1 Detection and edge scoring

`TemporalUNet3D` maps a movie tensor to a per-voxel center heatmap. Three-dimensional convolutions and skip connections combine local spatial detail with a larger receptive field, while temporal context uses persistence across frames. Non-maximum suppression and a sigmoid threshold convert the heatmap into candidate points. The archived configuration requires a dual-seed low-margin consensus: edge evidence is weighted `0.20` and secondary detections `0.80`.

For each adjacent-frame pair, detected points carry 33-dimensional features. `SimpleNodeTransformer` projects the two node sets and applies bidirectional cross-attention so each node is contextualized by the other frame. A pairwise multilayer perceptron then emits an edge probability from the contextual embeddings and relative coordinates. A `ForkHead` exists in the external support pack and can score parent/two-daughter proposals, but its contribution to the archived inference path was not verified.

### 2.2 Initial graph and post-link divisions

The edge probabilities and appearance, disappearance, and division costs feed an ILP with one-parent/two-child lineage constraints. In the archived configuration, flow-based motion relinking using learned edge probabilities can replace the ILP edge set wholesale; the ILP therefore supplies an initial graph rather than the final division graph. Final divisions come mainly from post-link safe-division geometry, orphan-division recovery, and pruning by a 10-model mitosis-classifier CNN ensemble. The archived path does not claim that `ForkHead` supplies those final divisions.

### 2.3 Active configuration

The retained configuration also includes position refinement at weight `0.5`, relink model override and low-probability pruning, bidirectional harmonic edge fusion at `0.15`, an 8-view test-time patch, line-fit smoothing, and mandatory mitosis-gate weights `s0` through `s9`. The source record's preregistered rule recommended variants 201 and 244 as a pair; the Kaggle UI selection is not recorded locally. Variant 244 carries a one-line publication-copy guard edit changing the expected disappearance value from 2 to 3.0 because its hashed source file declares 3 while checking 2.

## 3. Evidence and results

The official Kaggle leaderboard reports rank 51/3,947, Silver, private score 0.93486. The source record's component evaluations are summarized below.

| Evaluation | Result | Interpretation |
|---|---|---|
| KX, 27 held-out movies from one embryo (`6bba`) | Flow relinking `+0.0041`, 95% CI `[+0.0013,+0.0075]`; 18 wins / 8 losses / 1 tie | Paired evidence for flow relinking on predecessor PROBE-196, not either archived notebook. Readmission and gap filling had no held-out evidence; their in-sample read was `-0.0011` versus 196. |
| Fresh unseen-embryo evaluation, 20 movies, flow-only | `-0.0012`; 11 wins / 9 losses | The fresh read was negative; the source record attributes earlier positive selection to selection effects. |
| D3 difference, KX | `+0.0014`, 95% CI `[-0.0005,+0.0034]` | The 201-versus-244 difference was not CI-separated on KX. |
| D3 difference, fresh B′ | `-0.0017` | Fails the source rule “not lower on either unseen embryo.” |
| Fresh flow + D3 arm, 20 movies | `+0.0059`, 95% CI `[-0.0024,+0.0131]`; 12 wins / 8 losses | Called confirmed only under the preregistered threshold rule; the interval crosses zero. |

The KX and fresh evaluations re-solved an ILP from candidate dumps in a local harness, rather than executing the archived notebooks end to end. No local evaluation in this record shows a confidence-separated gain for either archived variant as a whole. The ranker is not part of either archived variant; a separate ranker evaluation included B′ movies in its M44 training set and is not clean whole-movie generalization evidence.

## 4. Limitations and reproducibility

This is an archival technical report, not a peer-reviewed study. The public package excludes competition data, learned weights, and support artifacts whose redistribution permission was not verified. A rerun needs a CUDA-capable Kaggle-style environment, the competition input, the linked public packs, and separately authorized corrected-detector, mitosis-gate, and refinement artifacts. Missing refinement, TTA, readmission, or gap-filler inputs can degrade through documented fallbacks; the corrected-detector artifact is not checksum-verified.

The KX result is a component comparison from 27 movies belonging to one embryo and a predecessor configuration, not a whole-pipeline score. Fresh flow-only evidence is negative, and the D3 interval crosses zero on KX while its fresh B′ read is negative. The official score is an external leaderboard outcome, not a local cross-validation estimate. Source and archive hashes are provided, but neither archived notebook is byte-mapped to the official scored submission.

## 5. References

All links were checked 2026-11-09.

1. Biohub - Cell Tracking During Development, official competition page: https://www.kaggle.com/competitions/biohub-cell-tracking-during-development
2. Official leaderboard: https://www.kaggle.com/competitions/biohub-cell-tracking-during-development/leaderboard
3. Official scorer and baseline model repository (BSD-3-Clause): https://github.com/royerlab/kaggle-cell-tracking-competition
4. Public base notebook, Apache-2.0 notice: https://www.kaggle.com/code/anvithpothula/biohub-0-953-lb-original
5. DeepCenter center-prior dataset, Kaggle API-reported CC0: https://www.kaggle.com/datasets/pilkwang/biohub-deepcenter-unet3d-center-prior-v1
6. Temporal U-Net dataset, Kaggle API-reported CC0: https://www.kaggle.com/datasets/pilkwang/biohub-temporal-unet3d-seed314159-v1
7. Tracking support pack, Kaggle API-reported CC0: https://www.kaggle.com/datasets/pilkwang/biohub-tracking-support-pack-50ep-v1
