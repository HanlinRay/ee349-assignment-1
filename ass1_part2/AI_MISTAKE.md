# AI Mistake Report

## Context

- **Agent:** Claude Code
- **Model:** Claude Opus 5
- **Effort:** High

I have more than one GitHub account, including `orkaYu` and `HanlinRay`.
While setting up my development environment, I wanted to switch my local setup
to use `HanlinRay`.

## What I Asked

Please change orkaYu to HanlinRay.

## What the AI Did

Claude changed my local Git identity so that the username became `HanlinRay`.

It treated this as if the GitHub account had been changed successfully.

## What Was Wrong

Git and GitHub have several separate settings.

`git config user.name` and `git config user.email` only control the name and
email stored in Git commits.

They do not determine which GitHub account is actually authenticated.

## How I Found Out

Claude responded: "change the account from Orkayu(hyu200308@gmail.com) to HanlinRay
(hyu200308@gmail.com) not HanlinRay(yuhanlin29@gmail.com)"

## Lesson

My request was too vague, and Claude made a reasonable-looking change at the
wrong level.

For setup tasks like this, I should be more specific about what I want and
verify the result directly.
