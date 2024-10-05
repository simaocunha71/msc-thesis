    # We use the fact that the largest coefficient is non zero
    # and the polynomial is even degree.
    # Let's denote the coefficients in decreasing order as follows:
    # c0 > 0, c1, c2, ... , cn
    # Then, the zero point x is such that:
    # c0 * x^n + ... + cn = 0
    # c0 * x^n + ... + cn = c0 * (x^n + ... + cn / c0) = 0
    # then, x = - (c1 / c0) + (c2 / c0) * x + ... + (cn / c0) * x^n
    # which is the same formula as poly(x)

    coeffs = xs[::-1]
    return round(poly(coeffs, -coeffs[0] / coeffs[1]), 2)

# Testing
# print(find_zero([1, 2]))
# print(find_zero([-6, 11, -6, 1]))
# print(find_zero([1, -1, 0]))
# print(find_zero([1]))
# print(find_zero([-1]))

# print(find_zero([1, 0, -1]))
# print(find_zero([1, 0, 0, 0]))
# print(find_zero([1, 0, 0]))
# print(find_zero([0, 0, 0]))
# print(find_zero([0]))


# Your code here


def find_zeros(xs: list):
    """ xs are coefficients of a polynomial.
    find_zeros find all zeros of the polynomial poly(x) = 0.
    find_zeros returns a list of zero points, even if there are many.
    """
    # We use the fact that the largest coefficient is non zero
    # and the polynomial is even degree.
    # Let's denote the coefficients in decreasing order as follows:
    # c0 > 0, c1, c2, ... , cn
    # Then, the zero points x are such that