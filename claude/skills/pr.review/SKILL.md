---
name: pr.review
description: Review the current branch's PR — code quality, accidental cruft, and test quality. Use when preparing to merge or asked to review a branch.
---

Review the current branch's PR using the following process. Use plain `git` commands for
anything git can answer; reach for `gh` only for PR metadata (description, comments, CI).

## 1. Gather the changes

Work out the base branch first — don't assume `main`:

```sh
gh pr view --json baseRefName,number,title,url,body 2>/dev/null   # if a PR exists
git symbolic-ref --short refs/remotes/origin/HEAD                 # fallback: origin's default branch
```

Then get the diff and the commit history, using `BASE` from above (e.g. `origin/main`):

```sh
git fetch origin --quiet
git diff $BASE...HEAD          # three-dot: fork point → HEAD
git log $BASE..HEAD --stat
```

The three-dot form diffs from the branch's **merge base** (where it diverged from the base
branch) to `HEAD`, so it captures only the changes actually made on this branch — never
changes that landed on the base branch after the branch was created. This holds even when
the branch is behind the latest base, so review whatever this diff shows without worrying
about rebasing first.

If there are uncommitted changes (`git status --short`), mention them but review the
committed diff — that's what the PR contains.

## 2. Cruft scan

Look at the file list from the diff (`git diff --stat $BASE...HEAD`). Flag anything that
probably shouldn't be committed:

- Notebook HTML output, generated PDFs/images outside `docs/` or `assets/`
- Binaries or archives (`.zip`, `.tar.gz`, `.pkl`, `.npy`, `.npz`)
- Large data files (`.csv`, `.tsv`, `.parquet` over 100KB)
- Cache/build artifacts (`__pycache__/`, `dist/`, `node_modules/`, `.ipynb_checkpoints/`)
- Secrets or local config (`.env`, credentials, absolute paths to your home directory)

Flag these in your report — don't block the rest of the review.

## 3. Read all changed files in full

For every file that appears in the diff, read the entire file (not just the diff hunks).
You need the surrounding context to review correctly.

## 4. Code review

Use the guidelines in CLAUDE.md (repo root and any nested ones covering changed files) to
complete your review. Skip praise and pleasantries — just report issues. I'm interested in
all issues you find, but pay **special attention** to:

- **Adherence to established patterns** — does the change follow the conventions,
  abstractions, and structure already used in this codebase, or does it reinvent /
  diverge from them?
- **Effective code reuse** — does it reuse existing functions, types, and utilities where
  it should, instead of duplicating logic?

If there are no issues, say so briefly. Do not feel obligated to find issues where none exist.

For every issue you report, you **must** include:
- The specific file path and line number
- A direct quote of the problematic code
- An explanation of the problem and a suggested fix

## 5. Test audit

Examine test files in the diff. Static greps miss these — read the bodies. Flag:

- Placeholder tests (empty bodies, `pass`-only, `assert True` / trivial assertions)
- Tests that catch and swallow exceptions instead of letting them propagate
- `pytest.skip` / `t.Skip` / `@pytest.mark.xfail` that should be real implementations
- Tests without meaningful assertions
- New behavior in the diff with no corresponding test

Report findings with severity (blocking vs advisory).

## 6. Report

Output the review as markdown in the conversation, organized as: cruft → blocking issues →
advisory issues → test audit. Do **not** post to GitHub unless I ask. If I do ask, use
`gh pr comment` for a single summary comment, or `gh pr review --comment` with inline
comments for line-level findings.

## Notes

- Assume all tests already pass.
- If the repo has a `pixi.toml`, run environment commands with `pixi run`.
- If no PR exists yet for this branch, review the branch anyway and say so.
