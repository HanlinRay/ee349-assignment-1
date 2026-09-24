import pytest

from calculator import add


def test_adds_two_positive_integers():
    assert add(2, 3) == 5


def test_adds_negative_numbers():
    assert add(-4, -6) == -10
    assert add(-4, 6) == 2


def test_zero_is_the_identity_element():
    assert add(0, 7) == 7
    assert add(7, 0) == 7


def test_addition_is_commutative():
    assert add(3, 9) == add(9, 3)


def test_adds_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize("bad", ["1", None, [1], True])
def test_rejects_non_numeric_arguments(bad):
    with pytest.raises(TypeError):
        add(bad, 1)
    with pytest.raises(TypeError):
        add(1, bad)
