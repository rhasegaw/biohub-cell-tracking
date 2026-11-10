# Biohub research results

Checked 2026-11-09. This document records source-backed results; no new training, simulation, competition run, or submission was performed while preparing the archive.

## Official outcome

The official Kaggle leaderboard reports:

| Field | Value | Source |
|---|---:|---|
| Competition | Biohub - Cell Tracking During Development | https://www.kaggle.com/competitions/biohub-cell-tracking-during-development |
| Final rank | 51 / 3,947 teams | https://www.kaggle.com/competitions/biohub-cell-tracking-during-development/leaderboard |
| Medal | Silver | Official leaderboard record |
| Private score | 0.93486 | Official leaderboard record |

The official record is an externally judged result, not a local validation score.

## Archived lineage and hashes

The source record's preregistered rule recommended variants 201 and 244 as a final pair; the selection made in the Kaggle UI is not recorded locally. Variant 201 contains the corrected-detector lineage. Variant 244 changes the declared ILP disappearance cost from 2 to 3.0. The 244 source file as hashed fails its own configuration guard (the source guard expects 2 while the environment declares 3), so the archived 244 includes a one-line guard edit (expected disappearance 2 → 3.0). Neither archived notebook is byte-mapped to the official scored submission.

The archived notebooks are cleaned copies of the two source notebooks. Their source and archive hashes are stored in `metadata/variant-201.json` and `metadata/variant-244.json`. The archive copy is not byte-identical to the source because it removes outputs, private authoring metadata, internal validator cells, private dataset-owner slugs, and stale internal notes.

| Variant | Source notebook SHA-256 | Archived notebook SHA-256 |
|---|---|---|
| 201 | `5ec0dea62c0a304f5529bfd7ddac77cff8040b859724917840a007cb771fafaa` | `6dd4a286a179a2266a75c9860917d33866a91ef0baa42df0039a15a69124cf04` |
| 244 | `3ef9670340cfa2528822ea4c12fb2bdc65040a3c156c8a246275b09e557df50b` | `ac506e773a696c911b64bfef03324a8787a8c8922cdbb8b1acc988b854e810cb` |

The archive hash is regenerated whenever the publication copy changes; the source hash is preserved from the original notebook.

## Validation evidence retained from the source record

| Evaluation | Result | Interpretation |
|---|---|---|
| KX, 27 held-out movies from one embryo (`6bba`) | Flow relinking `+0.0041`, 95% CI `[+0.0013,+0.0075]`; 18 wins / 8 losses / 1 tie | Paired component evidence for flow relinking on a predecessor configuration (PROBE-196), not evaluation of either archived notebook. Readmission and gap filling had no held-out evidence; their in-sample read was `-0.0011` versus 196. |
| Fresh unseen-embryo evaluation, 20 movies, flow-only | `-0.0012`; 11 wins / 9 losses | Negative fresh read; the source record attributes the earlier positive selection to selection effects. |
| D3 difference, KX | `+0.0014`, 95% CI `[-0.0005,+0.0034]` | The 201-versus-244 difference was not CI-separated on KX. |
| D3 difference, fresh B′ | `-0.0017`; fails the source rule “not lower on either unseen embryo” | Fresh evidence did not support the D3 change. |
| Fresh flow + D3 arm, 20 movies | `+0.0059`, 95% CI `[-0.0024,+0.0131]`; 12 wins / 8 losses | The source record calls this confirmed only under its preregistered threshold rule; the interval crosses zero. |

The KX and fresh evaluations re-solved an ILP from candidate dumps in a local harness; they were not full executions of the archived notebooks. No local evaluation in this record shows a CI-separated gain for either archived variant as a whole. The ranker is not part of either archived variant; a separate ranker evaluation included B′ movies in its M44 training set and is not clean whole-movie generalization evidence.

## Metric and task

The task detects and links nuclei in 3D+t zebrafish embryo volumes. The competition score is adjusted edge Jaccard plus `0.1 × division Jaccard`, using a 7 µm bipartite node match; the official scorer is linked at https://github.com/royerlab/kaggle-cell-tracking-competition.

## Reproducibility limits

The archive omits data and model artifacts, and the final official submission is not byte-mapped to either archived notebook. The corrected-detector artifact is not checksum-verified in the notebook. A future rerun should report its own asset hashes, notebook hash, environment, and official score separately from the result above.

The hashed 244 source would fail its own guard and is therefore not the executed kernel artifact. The archive additionally corrects stale print/comment strings in both variants.
