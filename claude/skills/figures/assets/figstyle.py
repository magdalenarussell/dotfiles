"""Shared figure style: Wilke-style defaults, colorblind-safe palettes, labeling helpers.

Vendor this module once per project (e.g. `<package>/plotting/figstyle.py`) and import
it from every plotting script. Do not copy individual settings into scripts.

Palettes follow Okabe-Ito, which stays distinguishable under all common forms of
color vision deficiency.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

# Okabe-Ito qualitative palette. Use in order; beyond five categories, switch to
# faceting, direct labeling, or an ordered encoding instead of more colors.
OKABE_ITO: dict[str, str] = {
    "orange": "#E69F00",
    "sky_blue": "#56B4E9",
    "green": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "purple": "#CC79A7",
    "black": "#000000",
}

CATEGORICAL: list[str] = [
    OKABE_ITO["blue"],
    OKABE_ITO["vermillion"],
    OKABE_ITO["green"],
    OKABE_ITO["orange"],
    OKABE_ITO["purple"],
    OKABE_ITO["sky_blue"],
]

SEQUENTIAL = "viridis"
DIVERGING = "RdBu_r"

# Vector formats figures may be saved as. PDF by default; SVG for figures that
# will be edited further in a vector editor.
VECTOR_FORMATS = frozenset({".pdf", ".svg"})

GRAY = "#B3B3B3"
ACCENT = OKABE_ITO["blue"]

# Widths in inches for a figure placed at final size without rescaling.
SINGLE_COLUMN = 3.42
DOUBLE_COLUMN = 7.0

_RC_PARAMS: dict[str, object] = {
    # Text sized for a figure used at its native size. Never shrink a figure in the
    # manuscript; make it smaller here instead.
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica", "Arial", "DejaVu Sans"],
    "font.size": 9,
    "axes.labelsize": 9,
    "axes.titlesize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    # Minimal frame: data, axes, labels, nothing else.
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.axisbelow": True,
    "axes.labelpad": 4.0,
    "xtick.direction": "out",
    "ytick.direction": "out",
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "xtick.major.size": 3.0,
    "ytick.major.size": 3.0,
    "legend.frameon": False,
    "legend.handlelength": 1.4,
    "legend.borderaxespad": 0.0,
    "lines.linewidth": 1.25,
    "lines.markersize": 4.0,
    "patch.linewidth": 0.0,
    "figure.figsize": (SINGLE_COLUMN, SINGLE_COLUMN * 0.75),
    "figure.dpi": 150,
    "savefig.dpi": 400,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
    "savefig.transparent": False,
    "savefig.format": "pdf",
    # Type 42 keeps text editable in vector output.
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "axes.prop_cycle": mpl.cycler(color=CATEGORICAL),
}


def use_style() -> None:
    """Apply the shared defaults. Call once, before creating any figure."""
    mpl.rcParams.update(_RC_PARAMS)


def direct_label(ax: Axes, x: float, y: float, text: str, color: str, **kwargs) -> None:
    """Label a series on the plot itself, replacing a legend entry."""
    ax.text(x, y, text, color=color, va="center", clip_on=False, **kwargs)


def highlight(categories: list[str], focus: str | list[str]) -> dict[str, str]:
    """Map each category to a color, graying out everything outside `focus`."""
    focused = [focus] if isinstance(focus, str) else focus
    accents = iter(CATEGORICAL)
    return {
        category: next(accents) if category in focused else GRAY
        for category in categories
    }


def identity_line(ax: Axes, **kwargs) -> None:
    """Draw a 1:1 reference line across the current limits and square the axes."""
    low = min(ax.get_xlim()[0], ax.get_ylim()[0])
    high = max(ax.get_xlim()[1], ax.get_ylim()[1])
    ax.plot([low, high], [low, high], color="black", lw=0.6, zorder=0, **kwargs)
    ax.set_xlim(low, high)
    ax.set_ylim(low, high)
    ax.set_aspect("equal")


def assert_untitled(fig: Figure) -> None:
    """Fail if any axes or the figure carries a title. Captions belong in the text."""
    if fig.get_suptitle():
        raise ValueError("Figure has a suptitle; describe the figure in its caption.")
    for index, ax in enumerate(fig.axes):
        if ax.get_title():
            raise ValueError(
                f"Axes {index} has title {ax.get_title()!r}; "
                "use an axis label or the caption instead."
            )


def save_figure(fig: Figure, save_path: str | Path) -> None:
    """Write a figure to disk as vector output, enforcing the no-title rule.

    Defaults to PDF when the path carries no extension; SVG is also accepted.

    Raises:
        ValueError: If the figure carries a title, or the format is not vector.
    """
    assert_untitled(fig)
    save_path = Path(save_path)
    if not save_path.suffix:
        save_path = save_path.with_suffix(".pdf")
    if save_path.suffix.lower() not in VECTOR_FORMATS:
        allowed = " or ".join(sorted(VECTOR_FORMATS))
        raise ValueError(
            f"Figures are saved as vector output ({allowed}), "
            f"not {save_path.suffix}: {save_path}. "
            "Raster output loses resolution and is not publication-ready."
        )
    save_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path)
    plt.close(fig)
