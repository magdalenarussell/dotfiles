# Global preferences

These apply to every project. Project-level `CLAUDE.md` files cover only what is
specific to that repo (environment, structure, domain) — if one repeats something
here, treat that as an oversight worth flagging, not as emphasis.

## Response style

- Keep responses short and targeted. Skip preambles ("I'll help you with...") and
  get straight to the answer or action.
- Bullet points over paragraphs for multi-part answers.
- Don't narrate tool use. Just do it.
- Match verbosity to the task: routine edits need almost no commentary; save
  explanation for complex logic and architectural decisions.

## Token efficiency

- Don't poll or re-read. Wait once for a background task to finish rather than
  repeatedly reading its output.
- After a tool succeeds, don't re-read to confirm it worked.
- Prefer one well-constructed command over three incremental checks.
- Background tasks return a completion notification whose `<result>` content is
  all that's needed. Never pull the full transcript of a finished task — it costs
  enormous context for nothing.

## Coding workflow

All substantive code work follows four steps, in order:

1. **Issue** — open a GitHub issue describing the problem or feature.
2. **Branch** — cut a new branch off the default branch to implement that issue.
3. **Draft PR** — open it as a draft, referencing the issue.
4. **Review** — run the `pr.review` skill, and expect to run it repeatedly until
   it comes back clean.

Two skills bracket the work: `task.start` for steps 1–2, `task.finish` for steps
3–4. Rules:

- **Recognize the entry point.** When asked to build, fix, change, or refactor
  something and none of this has started, say so and offer to begin at step 1
  before writing code.
- **Not every session is a task.** Plenty of sessions are discussion — thinking
  through a design, interpreting a result, asking how something works, or
  working inside a step already underway. Those need no issue. If which one it is
  is genuinely unclear, ask in one line rather than assuming either way.
- **Never post to GitHub unprompted.** Draft every issue body, PR description,
  and review comment locally and show it for approval first. This holds even
  mid-flow and even when the content seems obvious.
- **Don't skip ahead.** No branch without an issue, no PR without a branch.
  If something is already out of order, point it out instead of silently
  patching over it.

## GitHub issues and PR descriptions

Write for a person seeing the work for the first time. Concise, plain English.

- **No code identifiers, ever.** No function, class, variable, file, or module
  names — nothing in backticks. Describe behavior and intent instead: "renamed
  the time-tracking class to reflect that it now supports multiple axes", not
  "renamed `TimeTracker` to `MaturationTracker`". This applies every time,
  including in an "other changes" section, and whether or not I mention it.
- **Keep it short.** This applies to issue bodies and PR descriptions alike. A
  few sentences plus a handful of bullets is the target; a page of prose is not.
  Lately these have been far too verbose. Cut background the reader doesn't need,
  don't restate the same point in two places, and leave out anything a reviewer
  can see from the diff. An issue states the problem, why it matters, and what
  done looks like — nothing more.
- **No file-by-file breakdowns.** Summarize what changed and why.
- **Describe the branch as it stands off the default branch.** Reviewers don't
  need the iteration history — fixes made during development, dead ends, or
  review rounds.
- Propose a useful title at the top. No "# Summary" header; dive straight in.
- A PR that closes an issue opens with "This PR resolves #<n>".
- Order: what it addresses (often restatable from the issue) → summary of
  changes → experimental results, if any.
- Write the body to a file and pass it to `gh` with `--body-file`, never inline.

## Git commits

Write commit messages as a single one-line description — not full prose.

- One short imperative subject line summarizing the change. No body paragraphs.
- Skip the bulleted "what changed" rundown and the explanatory narrative.
- Attribution trailers (e.g. `Co-Authored-By:`) are not prose and still belong at the end.

Good: `adding replay validation`
Bad: a subject line followed by three paragraphs explaining the motivation and approach.

## Code style

Simplest, cleanest thing that works. Complexity needs a justification.

- **Duplication is the primary thing to avoid.** Before adding code, look for an
  existing function, type, or utility that already does it. Two copies of a rule
  means it's wrong in one of them eventually.
- **Follow established patterns.** Use the conventions and abstractions already
  in the codebase rather than introducing a parallel way to do the same thing.
- **Single responsibility.** Each function and class does one thing.
- **Small functions, intent-revealing names.** A name that explains itself beats
  a comment explaining a vague one.
- **Simplify relentlessly.** Challenge hardcoded decisions — ask whether a
  constraint is needed at all before building around it.
- **Minimal interfaces.** Push complexity out of core abstractions; prefer
  external composition over internal branching.
- **Composition over configuration.** A parameter that selects from a menu of
  behaviors (string flags, enums, `if mode ==` chains) should usually be an
  injected behavior object instead.
- **Complete type annotations** on all functions and classes.
- **Imports at module top**, after the docstring, in PEP 8 order (standard
  library, third-party, local). Specific imports, never star imports. Defer an
  import inline only for a heavy or optional dependency, with a comment saying why.

### Breaking changes are encouraged

Current projects have no external dependents. So: no backward-compatibility
constraints, no re-exports (import from the specific module), and **no migration
code** — if migration code seems necessary, stop and ask. If a test fails because
a fixture uses an old format, ask me to regenerate the fixture.

If a project does acquire outside users, its own `CLAUDE.md` overrides this.

## Naming

- `num_x` for every countable quantity: `num_layers`, `num_sites`, `num_sequences`.
- `_list` for variable-length Python lists; `_batch` for uniform tensors with a
  batch dimension.
- Variables reveal intent: `evolutionary_loss_weight`, not `w1`.
- Functions match behavior: `optimize_branch_lengths()`, not `update_data()`.
- Classes are concepts: `Trainer`, not `Manager`.
- Booleans are questions: `has_structural_data`, not `structural`.
- `_path` suffix for all filesystem paths, with an action prefix:
  `checkpoint_save_path`, `model_load_path` — not bare `path`.
- `dataset_nickname` for string identifiers, `dataset_name` for display,
  `dataset_path` for location. Likewise `model_config` for configs,
  `config_name` for its identifier.
- Specific component type plus `_name`: `head_name`, `encoder_name` — not `name`.
- Apply a pattern consistently across a collection. Don't mix
  `train_data_nicknames` with `head_names`.

## Docstrings and comments

- Concise, like the code. Google style, with Args/Returns/Raises only where they
  add something.
- Every non-trivial function and class gets one. Skip it for one-liners whose
  name already says everything.
- Document what the code does and the design behind it — not why it's good. No
  "advantages" or "benefits" lists, no meta-commentary.
- Include real domain context where it matters: the mathematical formula, the
  biological meaning, the algorithmic detail.
- Update docs the moment a design changes. Stale docs are worse than none.
- **No design-doc headers.** Never add "Design References", "Implementation
  Status", "Last Design Review" or similar bookkeeping to a module docstring, and
  don't keep separate design documents for code to cite. A module docstring says
  what the module does. Design rationale belongs next to the code it explains.

## Error handling

- **Fail fast and loudly.** Stop execution the moment something is wrong.
- **No silent fallbacks.** `raise ValueError(f"Required model {model_name} not found")`
  — never quietly substitute the first available option.
- Error messages say what failed and what was expected.
- Validate inputs at system boundaries.

## Testing

- **Real tests only.** Tests validate actual behavior. Identity functions,
  trivial arithmetic, and hardcoded returns are forbidden.
- **Never skip.** No `pytest.mark.skip`, no `pytest.skip` inside a test, no
  `xfail` standing in for a real implementation, no placeholder tests for
  unimplemented features.
- **Every test asserts something meaningful** about real system behavior. Tests
  exist to establish correctness, not coverage.
- **The urge to fake is a design smell.** If a thought starts with "I'll just
  mock this to return..." — stop. Difficult-to-test code usually means the design
  needs work. Ask rather than faking.
- New behavior in a diff needs a corresponding test.
- **No tests for plotting code.** Don't write tests that exercise figure or
  plotting functions — not for the plot itself, its styling, or whether it saves.
  If plotting code contains a real calculation (a summary statistic, a transform,
  a binning or normalization step), pull that out and test it on its own.
- Unit tests for components in isolation, integration tests for interactions,
  hypothesis for property-based testing where it fits.

## Figures

Load the `figures` skill before writing or editing any plotting code — always, not
only when a figure is the main task. In short: Python, matplotlib, Claus Wilke's
*Fundamentals of Data Visualization* principles, the shared style module, **vector
output (PDF or SVG), never PNG**, **no plot titles**, and short axis labels.

## Task management and scope

- **No time estimates.** Don't predict how long anything will take.
- **Binary priority.** Work is either active now or deferred to a future issue.
  No "critical"/"high"/"low" labels.
- Issues are scoped by clear acceptance criteria, not priority rankings.

## Local files

Any markdown written for my eyes rather than the repo — issue drafts, PR bodies,
notes, scratch analysis — goes in `temp_notes/<descriptive-subdirectory>/` with a
descriptive filename.
