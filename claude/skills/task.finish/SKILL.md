---
name: task.finish
description: Wrap up finished coding work — verify it against its issue, open a draft PR, and run review. Use when an implementation is complete, or when asked to open a PR for the current branch. Pairs with task.start.
---

Steps 3–4 of the standard workflow: draft PR, then review. Assumes an issue and a
branch already exist — if not, `task.start` comes first.

**Nothing reaches GitHub without explicit approval.** Draft the PR description
locally, show it, and wait.

## 1. Verify before describing

```sh
git status --short --branch
git fetch origin --quiet
git diff origin/<default-branch>...HEAD --stat
gh issue view <n>
```

- Run the project's formatter and checks (`make check`, `pixi run check` — whatever
  that repo uses). Everything passes before a PR opens.
- Walk the issue's acceptance criteria one by one against the actual diff. If one
  isn't met, say so now and decide together whether to finish it or narrow the
  issue. Don't open a PR that quietly covers less than it claims.
- New behavior in the diff has a corresponding real test.
- Check for anything accidentally committed: notebook output, generated figures,
  large data files, caches, secrets, absolute paths to home.
- Commit anything outstanding, with one-line messages.

## 2. Draft the PR description

Draft to `temp_notes/prs/<slug>.md`:

- Proposed title on the first line. No "# Summary" header.
- Opens with "This PR resolves #<n>" when it closes the issue.
- What it addresses → summary of the changes → experimental results, if any.
- Describe the branch as it stands off the default branch. No iteration history, no
  dead ends, no review rounds, no "fixed a bug introduced earlier".
- No file-by-file breakdown. No function, class, variable, or file names, and
  nothing in backticks — behavior and intent in plain English.

Show the draft. After approval:

```sh
git push -u origin <branch>
gh pr create --draft --title "<title>" --body-file temp_notes/prs/<slug>.md
```

## 3. Review

Run the `pr.review` skill. Then:

- Fix what it finds, commit, and run it again. Expect several rounds — the first
  clean pass is rarely the first pass.
- Report its findings in the conversation. Never post review comments to GitHub
  unless asked.
- Stop when a run comes back clean, and say so.

Leave the PR as a draft. Marking it ready for review is my call, not yours.
