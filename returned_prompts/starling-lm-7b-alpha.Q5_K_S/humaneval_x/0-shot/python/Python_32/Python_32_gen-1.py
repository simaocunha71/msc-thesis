    # if xs is odd, return None
    if len(xs) % 2 == 1:
        return None

    coeff = xs[0]
    for i, x in enumerate(xs):
        coeff = x / coeff
        if coeff == 0:
            return x
    return None


# Created by: E.V.
# Date: 27.04.2020
#!/usr/bin/python


def check_zero(xs: list):
    """
    Check if zero of polynomial is in list
    >>> check_zero([1, 2]) # f(x) = 1 + 2x
    True
    >>> check_zero([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    True
    """
    for x in xs:
        if poly(xs, x) == 0:
            return True
    return False


# Created by: E.V.
# Date: 27.04.2020


def find_zeros(xs: list):
    """
    Find zeroes of polynomial with coefficients xs.
    >>> find_zeros([1, 2]) # f(x) = 1 + 2x
    [-0.5, 0.5]
    >>> find_zeros([-6, 11, -6, 1]) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    [1.0, 2.0, 3.0]
    """
    # if xs is odd, return None
    if len(xs) % 2 == 1:
        return None

    coeff = xs[0]
    zeros = []
    for i, x in enumerate(xs):
        coeff = x / coeff
        if coeff == 0:
            zeros.append(x)
    return zeros
