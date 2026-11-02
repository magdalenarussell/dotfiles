---
name: task.start
description: Begin a piece of coding work — open an issue and cut a branch for it. Use when starting a new feature, fix, or refactor, or when picking up an existing issue. Pair with task.finish once the work is done.
---

Steps 1–2 of the standard workflow: issue, then branch. Implementation follows.
When the work is done, `task.finish` opens the draft PR.

**Nothing reaches GitHub without explicit approval.** Draft the issue body locally,
show it, and wait.

## 0. Orient

```sh
git rev-parse --show-toplevel             # confirm a repo
git status --short --branch
git symbolic-ref --short refs/remotes/origin/HEAD
gh issue list --limit 15
```

Resolve three things before drafting anything:

- **Is this actually a task?** If the request is a question, a design discussion, or
  interpreting a result, this skill doesn't apply — say so and just talk.
- **Does an issue already exist?** If one covers this, skip to step 2 and use it.
  Don't open a duplicate.
- **Is the starting state clean?** Uncommitted changes on the default branch, or a
  branch that already exists for this work, mean stopping and pointing that out
  rather than building on an unclear state.

If the project has a `CLAUDE.md`, read it before drafting — scope conventions and
environment commands live there.

## 1. Issue

Understand the problem well enough to state it plainly. Read the relevant code
first; a vague issue produces vague work.

Draft to `temp_notes/issues/<slug>.md`:

- A proposed title on the first line.
- What the problem or desired behavior is, in plain English.
- Acceptance criteria — what's true when this is done.
- No function, class, variable, or file names. No backticked identifiers. Describe
  behavior and intent.
- No time estimates, no priority labels.

Show the draft. After approval:

```sh
gh issue create --title "<title>" --body-file temp_notes/issues/<slug>.md
```

## 2. Branch

Match the repo's existing convention (`git branch -a --sort=-committerdate`);
default to `dev-<short-slug>`.

```sh
git fetch origin --quiet
git switch -c dev-<slug> origin/<default-branch>
```

Report the issue URL and the branch name, then implement — following the code
standards in `CLAUDE.md` and committing in logical units with one-line messages.

Keep the issue's acceptance criteria in view while working. If one turns out to be
wrong or unreachable, raise it rather than quietly dropping it.
