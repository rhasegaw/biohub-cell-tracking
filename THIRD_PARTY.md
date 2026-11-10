# Third-party provenance and redistribution boundary

Checked 2026-11-09.

## Code derived from or embedded

The retained notebook lineage includes portions derived from the public Kaggle notebook **Biohub 0.953 LB | ORIGINAL**:

- https://www.kaggle.com/code/anvithpothula/biohub-0-953-lb-original

That page states Apache-2.0. The archive keeps the attribution, carries the license text in `licenses/Apache-2.0.txt`, and marks the publication copy as modified. Apache-2.0 obligations continue to apply to code derived from that notebook.

The notebooks also use source fragments and runtime patch anchors materialized from the `biohub-tracking-support-pack-50ep-v1` dataset:

- https://www.kaggle.com/datasets/pilkwang/biohub-tracking-support-pack-50ep-v1

The Kaggle API reported CC0 for that dataset on the checked date, but the dataset's source-code origin is not separately exposed in the record inspected here. The archive links the pack rather than redistributing it.

The `TemporalUNet3D` and `SimpleNodeTransformer` baseline origin was verified in the official repository:

- https://github.com/royerlab/kaggle-cell-tracking-competition

That repository is BSD-3-Clause; the checked license text is retained in `licenses/BSD-3-Clause.txt`. The repository is also the source reference for the competition scorer. Adaptations predating the cited 0.953 notebook are treated as the author's own additions; no separate upstream origin was verified for them.

## Public model/support datasets

Kaggle's dataset API reported `CC0: Public Domain` for each linked external dataset on the checked date:

- https://www.kaggle.com/datasets/pilkwang/biohub-deepcenter-unet3d-center-prior-v1
- https://www.kaggle.com/datasets/pilkwang/biohub-temporal-unet3d-seed314159-v1
- https://www.kaggle.com/datasets/pilkwang/biohub-tracking-support-pack-50ep-v1

The datasets are linked, not copied into this repository. Their current terms and contents should be rechecked before redistribution or commercial use.

## Omitted assets and author additions

Corrected detector weights, edge-predictor weights, mitosis-gate weights, refinement weights, competition data, and any artifact without a verified public redistribution permission are intentionally omitted. The notebooks treat them as external prerequisites. No license is granted for the author's own additions pending explicit publication approval.

The re-implemented DeepCenter model definition follows the architecture in the [DeepCenter center-prior pack](https://www.kaggle.com/datasets/pilkwang/biohub-deepcenter-unet3d-center-prior-v1), whose reported CC0 terms are recorded above.
