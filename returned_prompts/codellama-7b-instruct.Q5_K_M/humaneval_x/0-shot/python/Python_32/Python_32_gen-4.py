import math


def poly(xs, x):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))


def find_zero(xs):
    assert len(xs) % 2 == 0
    assert max(xs) != 0
    for i in range(len(xs)):
        if xs[i] != 0:
            return -xs[i] / xs[i + 1]


def test_find_zero():
    assert find_zero([1, 2]) == -0.5
    assert find_zero([-6, 11, -6, 1]) == 1
    assert find_zero([1, 2, 3]) == -3
    assert find_zero([1, 2, 3, 4]) == -6


if __name__ == "__main__":
    test_find_zero()
