from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS = [ROOT / "notebooks" / "biohub-variant-201.ipynb", ROOT / "notebooks" / "biohub-variant-244.ipynb"]
METADATA = {
    "201": ROOT / "metadata" / "variant-201.json",
    "244": ROOT / "metadata" / "variant-244.json",
}
EXPECTED_SOURCE_HASHES = {
    "201": "5ec0dea62c0a304f5529bfd7ddac77cff8040b859724917840a007cb771fafaa",
    "244": "3ef9670340cfa2528822ea4c12fb2bdc65040a3c156c8a246275b09e557df50b",
}
FORBIDDEN = re.compile(r"(?i)(?<![A-Za-z0-9])(?:C:[/\\]Users|G:[/\\]|D:[/\\])")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    assert all(path.is_file() for path in NOTEBOOKS), "archived notebooks are missing"
    for path in NOTEBOOKS:
        notebook = json.loads(path.read_text(encoding="utf-8"))
        assert notebook.get("nbformat") == 4, path
        assert all(key not in notebook.get("metadata", {}) for key in ("authoring", "runtime_trace", "source_receipt")), path
        variant = path.stem.rsplit("-", 1)[-1]
        record = json.loads(METADATA[variant].read_text(encoding="utf-8"))
        assert record["source_notebook_sha256"] == EXPECTED_SOURCE_HASHES[variant], path
        assert record["archived_notebook_sha256"] == sha256(path), path
        all_text = []
        for cell in notebook.get("cells", []):
            assert cell.get("metadata", {}) == {}, path
            text = "".join(cell.get("source", []))
            all_text.append(text)
            if cell.get("cell_type") == "code":
                assert cell.get("outputs", []) == [], path
                assert cell.get("execution_count") is None, path
        joined = "\n".join(all_text)
        assert not FORBIDDEN.search(joined), path
        assert "TemporalUNet3D" in joined, path
        assert "SimpleNodeTransformer" in joined, path
        assert "ILP" in joined, path
        assert "Biohub 0.953 LB | ORIGINAL" in joined, path
        assert "submission.csv" in joined, path
    print(f"archive smoke test passed: {len(NOTEBOOKS)} notebooks")


if __name__ == "__main__":
    main()
