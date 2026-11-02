# Choosing and checking a figure

Decision rules distilled from Claus Wilke, *Fundamentals of Data Visualization*.
Start from the question the figure answers, not from the chart type.

## Amounts

One value per category.

- **Bars** — zero baseline, sorted by value, horizontal when labels are long (never
  rotate x labels to fit).
- **Dot plot** — when zero isn't meaningful or the values cluster in a narrow range
  far from zero. Preferred over a truncated bar axis.
- **Heatmap** — two categorical axes with one value per cell. Order rows and columns
  by similarity or magnitude, not alphabetically.
- **Grouped bars** — at most two levels, and only when comparing within a group is
  the point. Beyond that, facet.
- Stacked bars only when the total is itself meaningful.

## Distributions

- **Histogram** — report the bin width; try several, since the shape depends on it.
- **Density** — smooth and compact, but it invents support beyond the data. Set
  sensible bounds for quantities that can't go negative.
- **ECDF / q-q** — no tuning parameter, honest about every data point. Best for
  comparing a few distributions or checking a distributional assumption.
- **Boxplot** — only for large n. It hides bimodality and sample size.
- **Violin / sina / jittered points** — comparing several groups. With small n, show
  the individual points; with moderate n, points over a violin.
- **Ridgeline** — many distributions compared along a shared axis, especially over
  time or an ordered grouping.

## Proportions

- **Stacked bars** — a few categories, or proportions across groups.
- **Pie** — only for two or three slices where "part of a whole" is the entire
  message. Otherwise avoid.
- **Mosaic / treemap** — proportions nested within groups.
- **Side-by-side bars of proportions** — when comparing one category across groups
  matters more than the whole.
- Don't use stacked areas or bars to compare trends in the middle series — only the
  bottom series has a straight baseline, so the rest are unreadable.

## x–y relationships

- **Scatter** — two continuous variables. Same units on both axes means a square
  aspect ratio and a 1:1 line (`identity_line`).
- **Line** — only when x has a meaningful order (time, dose, position). Never connect
  unordered points.
- **Paired data** — slope graph or a scatter against the 1:1 line, not two separate
  distributions.
- **Trend line** — LOESS or a fitted model, with its confidence band. Say which in
  the caption. Don't fit a line to data that isn't linear just to have a line.
- **Log scale** — when the data spans orders of magnitude or the meaningful change is
  multiplicative. Label ticks in original units (1, 10, 100), not exponents.
- **Aspect ratio** — aim for line slopes near 45°; a nearly flat or nearly vertical
  trend is hard to judge.

### Overplotting

In order of preference as n grows: transparency (`alpha`) → jitter, for discrete or
rounded values, stating the jitter amount → 2D density contours → hex binning →
sampling as a last resort, said plainly in the caption.

## Uncertainty

- Always say what an interval means — standard error, standard deviation, or a
  confidence interval at a stated level. An unlabeled error bar is uninterpretable.
- **Points with intervals**, never bars with error bars on top.
- Graded error bands or multiple nested intervals communicate a distribution better
  than one hard cutoff.
- Confidence bands on fits are shown, not implied.
- Don't show an interval computed from so few points that it's meaningless — show
  the points.

## Checklist before saving

1. No plot title, no suptitle.
2. Axis labels are short noun phrases, with units where they exist.
3. Every bar starts at zero; no truncated bar axis.
4. Color serves one of the three purposes, and the palette matches that purpose.
5. Five or fewer categorical colors.
6. Series are directly labeled, or the legend order matches the data order.
7. Color meaning is redundantly coded (shape, line style, or label).
8. No dual y-axes, no 3D, no decorative gridlines or background.
9. Categories and panels ordered by something meaningful.
10. Figure is at final print size; all text is legible at that size.
11. Overplotting is addressed, and any sampling or jitter is disclosed.
12. Uncertainty is labeled with what it represents.
13. Scales are shared across facets, or the difference is called out.
14. Saved as vector output (PDF, or SVG) through `save_figure` — never PNG or raster.
