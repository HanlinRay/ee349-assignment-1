# AI Mistake Report

## Context

- **Agent:** Claude Code
- **Model:** Claude Opus 5
- **Effort:** High

I maintain more than one GitHub account, including `orka` and `HanlinRay`.
While setting up a development environment on this machine, I asked a coding
agent to move my local Git/GitHub configuration over to the `HanlinRay`
account. The mistake below occurred during that configuration work.

## What I Asked

The exact original wording was not preserved. In substance, I asked the agent
to switch my local Git/GitHub setup from my other GitHub account to HanlinRay.

## What the AI Did

The agent modified Git's identity configuration — the `user.name` and
`user.email` values — and reported the account switch as complete. In other
words, it made a change at the commit-metadata layer and treated that layer as
representing the requested account change.

That is the only verified behavior. The agent did not perform, and did not
verify, an authentication change against GitHub itself.

## What Was Wrong

The request spanned three separate mechanisms that the agent collapsed into
one:

1. **Git commit identity** — `user.name` and `user.email`. These are local
   settings. Git stamps them into commit objects as text. Git never validates
   them against anything; I can set them to any string I like.

2. **GitHub authentication** — which GitHub account my credentials actually
   authenticate as, held by the credential helper or `gh`'s token store. This
   is what determines whether a push is permitted and which account GitHub
   attributes the action to.

3. **Git remote destination** — where `origin` points, i.e. which repository
   on which account receives the push.

Changing (1) has no effect on (2) or (3). Writing `HanlinRay` into
`user.email` does not authenticate anything; it only changes the name printed
next to future commits. A setup edited this way can appear correct in
`git config` while still pushing — or failing to push — under an entirely
different account, or under no account at all.

## How I Found Out

I checked the authentication layer directly instead of trusting the
configuration layer:

```
$ gh auth status
You are not logged into any GitHub hosts.
```

No GitHub host was authenticated. Since there was no authenticated session at
all, the earlier identity edit could not possibly have constituted an
authenticated account switch — there was nothing to switch. The reported
success described a change to commit metadata only.

Re-checking after actually authenticating confirmed the distinction: once
`gh auth status` reported an active account and `gh api user` returned
`"login": "HanlinRay"`, the account was genuinely in effect — a state no
amount of `git config` editing had produced.

## Failure Mode

Conflation of Git commit identity with GitHub authentication state.

## Lesson

A configuration change has to be verified at the layer where the intended
effect actually occurs, not at whichever layer was most convenient to edit.
The goal here lived in GitHub's authentication state, so the check had to be
`gh auth status` and `gh api user` — not `git config --list`. Reading back the
value you just wrote confirms only that the write succeeded; it says nothing
about whether the write accomplished the goal. When a request touches several
layers that share a vocabulary — "identity", "account", "user" all appear in
Git and in GitHub — naming which layer each change lands in is what keeps a
plausible-looking edit from passing as a completed task.
