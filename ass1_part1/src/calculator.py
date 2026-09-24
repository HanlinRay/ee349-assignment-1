"""A deliberately trivial module.

The point of Part 1 is to exercise the toolchain (Git, GitHub, Docker,
Make, a coding agent), not to write interesting Python.
"""


def add(a, b):
    """Return the sum of two numbers.

    Args:
        a: A number (int or float).
        b: A number (int or float).

    Returns:
        The sum of ``a`` and ``b``.

    Raises:
        TypeError: If either argument is not an int or a float.
    """
    for name, value in (("a", a), ("b", b)):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be an int or a float, got {type(value).__name__}")
    return a + b
