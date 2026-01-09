"""Utility helpers for the Talent Retention Puzzle project."""

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = PROJECT_ROOT / "data" / "raw"
OUTPUTS = PROJECT_ROOT / "outputs"
FIGURES = PROJECT_ROOT / "reports" / "figures"

def ensure_dirs() -> None:
    """Create expected output directories."""
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
