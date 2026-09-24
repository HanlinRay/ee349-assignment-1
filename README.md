# EE349 — Assignment 1

Two independent parts.

## `ass1_part1/` — Development environment verification

Demonstrates a working development environment: **Git, GitHub, Docker, Make,
and a coding agent.** The Python program is deliberately trivial (`add(a, b)`
plus a pytest suite) because the toolchain is what is being verified, not the
code.

```bash
cd ass1_part1
make verify
```

`make verify` runs pytest locally, builds the Docker image, and runs pytest
again inside the container. It exits nonzero if any stage fails.

## `ass1_part2/` — Real AI mistake report

[`ass1_part2/AI_MISTAKE.md`](ass1_part2/AI_MISTAKE.md) documents an actual
mistake a coding agent made while configuring Git/GitHub: it changed Git
commit identity (`user.name` / `user.email`) and treated that as though it had
switched the authenticated GitHub account. Later verification with
`gh auth status` showed no GitHub host was authenticated at all.
