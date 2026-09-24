# Part 1 — Development Environment Verification

This part exists to prove that my development environment works end to end:
**Git, GitHub, Docker, Make, and a coding agent.**

The Python program is intentionally trivial — it is the toolchain, not the
algorithm, that is under test.

## What the code does

`src/calculator.py` exposes a single function:

```python
add(a, b)   # returns a + b; raises TypeError on non-numeric input
```

`tests/test_calculator.py` covers positive integers, negative numbers, the
zero identity, commutativity, float tolerance, and rejection of non-numeric
arguments (including `bool`, which is a subclass of `int`).

## Layout

```
ass1_part1/
├── Dockerfile          # python:3.11-slim image that runs the tests
├── Makefile            # test / docker-build / docker-test / verify
├── README.md
├── pytest.ini          # puts src/ on the import path
├── requirements.txt    # pytest
├── src/calculator.py
└── tests/test_calculator.py
```

## Usage

```bash
make test           # run pytest locally
make docker-build   # build the Docker image
make docker-test    # run pytest inside the container
make verify         # all three, in order
```

`make verify` runs the local test suite, builds the image, and runs the test
suite again inside the container. Make stops at the first failing step, so the
target exits nonzero if any stage fails and zero only if every stage passes.

## Requirements

- Python 3.11+ with `pytest` (`pip install -r requirements.txt`)
- Docker (daemon running)
- GNU Make
