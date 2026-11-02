---
name: figures
description: Read BEFORE writing or editing any figure, plot, or chart code in a project — anything that imports matplotlib, seaborn, plotnine or plotly, calls plt/subplots/savefig, or produces a panel, axis, legend, colormap or saved figure file, in a script, module or notebook. Also when revising, restyling or re-saving an existing figure. Python and matplotlib only, following Claus Wilke's Fundamentals of Data Visualization. Triggers on: plot, figure, chart, graph, panel, axis, visualize, colormap, palette, scatter, histogram, heatmap, boxplot, savefig.
---

Figures are built in Python with matplotlib, as simply as the data allows, following
the principles in Claus Wilke's *Fundamentals of Data Visualization*
(https://clauswilke.com/dataviz/).

## Non-negotiables

- **No plot titles.** No `set_title`, no `suptitle`. What a figure shows belongs in
  its caption in the manuscript or notebook prose. `save_figure` enforces this.
- **Concise axis labels.** A short noun phrase with units: "Mutations per site",
  "Days post-infection". Not a sentence, not a restated variable name
  (`num_mutations_per_site`), not a bare symbol with no referent.
- **Vector output, never PNG.** PDF by default, or SVG for a figure to be edited
  further in a vector editor. `save_figure` rejects raster formats. Raster only if
  I explicitly ask for it.
- **Python and matplotlib.** No R, no ggplot, no plotly.
- **The shared style module, not per-script settings.** Never paste rcParams or hex
  codes into a plotting script.

## Set up the style module first

Check whether the project already vendors the style module — look for `figstyle.py`
or a `plotting/` module in the package, and grep for `rcParams` or hardcoded hex
colors to find settings that should be consolidated there.

If it exists, import it. If not, copy `assets/figstyle.py` from this skill to
`<package>/plotting/figstyle.py` and mention that it's now the single place for
figure defaults. If the project has its own established plotting helpers, extend
those instead of adding a second system.

```python
from mypackage.plotting import figstyle

figstyle.use_style()        # once, before any figure
fig, ax = plt.subplots()
...
figstyle.save_figure(fig, output_path)   # vector output, checks for titles
```

It provides: `use_style`, `direct_label`, `highlight`, `identity_line`,
`save_figure`, the `OKABE_ITO` and `CATEGORICAL` palettes, `SEQUENTIAL`,
`DIVERGING`, `GRAY`, `ACCENT`, and `SINGLE_COLUMN` / `DOUBLE_COLUMN` widths.

## Core principles

**Proportional ink.** The filled area must be proportional to the value it
represents. Bars therefore start at zero, always. If zero isn't a meaningful
baseline or would waste the whole range, use a dot plot — don't truncate a bar axis.

**Remove everything that isn't data.** No gridlines unless a reader needs to read
values off the axis (then light horizontal only), no background fill, no 3D, no
shadows, no gradients, no boxes around legends.

**Direct labeling beats legends.** Put the series name next to the series. A legend
is a lookup table the reader has to hold in their head. When a legend is
unavoidable, order its entries to match the visual order of the data.

**Color has exactly three jobs** — distinguish categories, represent values, or
highlight. Decide which one before choosing a palette, and never use color
decoratively.
- Distinguish: `CATEGORICAL` (Okabe-Ito), five categories at most. More than that
  means facet, or encode the ordering instead.
- Represent values: `SEQUENTIAL` for one-directional magnitude, `DIVERGING` for
  deviation from a meaningful midpoint. Never a rainbow or jet map.
- Highlight: `highlight()` — accent what matters, gray out the rest.

**Redundant coding.** When color carries meaning, pair it with shape, line style, or
direct labels so the figure survives grayscale printing.

**Never use dual y-axes.** They invite arbitrary conclusions. Use two panels sharing
an x-axis, or plot a ratio.

**Size for final use.** A figure is drawn at the size it will be printed, using
`SINGLE_COLUMN` or `DOUBLE_COLUMN`. Never shrink a figure afterward — that shrinks
the text with it. If labels don't fit, simplify the figure.

**Facet rather than overload.** Small multiples with shared, consistent scales beat
one dense panel. Order panels by something meaningful (magnitude, time), never
alphabetically by accident.

**Order deliberately.** Bars and categories sort by value unless the categories have
a natural order. Alphabetical ordering is almost never the informative one.

## Choosing the form

See `references/wilke-principles.md` for the decision rules by question type
(amounts, distributions, proportions, x–y relationships, uncertainty), the
overplotting remedies, and the pre-save checklist. Read it when the chart type isn't
already obvious, when the data has more than a couple of dimensions, or when showing
uncertainty.

Two traps worth stating up front:

- **Never a bar chart of means.** It hides the distribution and the sample size. Show
  the points, or a distribution summary with the points over it.
- **Never a bar with an error bar on top** ("dynamite plot"). Use points with
  intervals.

## Before saving

Run through the checklist in `references/wilke-principles.md`. Then state in one
line what the figure shows and what was left out — that line is the draft caption.
