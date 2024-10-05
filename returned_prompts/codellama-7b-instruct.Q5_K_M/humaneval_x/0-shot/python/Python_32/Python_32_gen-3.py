import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    n = len(xs) - 1
    if n % 2 != 0 or xs[n] == 0:
        raise ValueError(
            "The list must have even length and have a non-zero coefficient at the highest power."
        )
    return -xs[n] / xs[n - 1]


def test_find_zero(coefs: list):
    """
    coefs: list of coefficients
    """
    # test that the function is correct
    x = find_zero(coefs)
    assert poly(coefs, x) == 0
    # test that the function is robust
    x = find_zero([0] * len(coefs))
    assert poly(coefs, x) == 0
    x = find_zero([0] * (len(coefs) - 1))
    assert poly(coefs, x) == 0
    # test