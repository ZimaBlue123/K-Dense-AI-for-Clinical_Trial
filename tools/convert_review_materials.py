from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    try:
        from markitdown import MarkItDown
    except Exception as e:  # pragma: no cover
        print(f"ERROR: markitdown import failed: {e}", file=sys.stderr)
        return 2

    root = Path(r"E:\Cursor Project\Scientific-Skills-for-Clinical_Trial\review_materials")
    if not root.exists():
        print(f"ERROR: directory not found: {root}", file=sys.stderr)
        return 2

    out_dir = root / "_converted_md"
    out_dir.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in root.iterdir() if p.is_file() and p.suffix.lower() in {'.docx', '.xlsx'}])
    if not files:
        print("ERROR: no .docx/.xlsx files found", file=sys.stderr)
        return 2

    md = MarkItDown()
    failures: list[tuple[Path, str]] = []

    for p in files:
        try:
            result = md.convert(str(p))
            text = result.text_content or ""
            out_path = out_dir / f"{p.name}.md"
            out_path.write_text(text, encoding="utf-8")
            print(f"OK: {p.name} -> {out_path.name}")
        except Exception as e:  # pragma: no cover
            failures.append((p, str(e)))
            print(f"FAIL: {p.name}: {e}", file=sys.stderr)

    if failures:
        print("\nFailures:", file=sys.stderr)
        for p, msg in failures:
            print(f"- {p.name}: {msg}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

