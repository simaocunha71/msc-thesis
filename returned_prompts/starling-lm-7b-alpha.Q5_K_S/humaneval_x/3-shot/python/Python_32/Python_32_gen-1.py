    # largest coefficient is at the end of the list
    coeffs = list(reversed(xs))
    # remove all coefficients smaller than the largest one
    while coeffs[0] == 0:
        del coeffs[0]
        del coeffs[-1]
    # if there are no coefficients left, return 0
    if len(coeffs) == 0:
        return 0
    # if there is only one coefficient left, it's the result
    if len(coeffs) == 1:
        return -coeffs[0] / coeffs[1]

    # find zero of the polynomial of the form ax^2 + bx + c = 0
    # quadratic formula ax^2 + bx + c = 0 gives us two solutions
    # however we need only one, so we pick the one smaller than 1
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return -c / a
    else:
        # discriminant is always non-negative
        # because of the while loop above
        return (-b + math.sqrt(discriminant)) / (2 * a)


# tests for find_zero
def test_find_zero():
    assert round(find_zero([1, 2]), 2) == -0.5
    assert round(find_zero([-6, 11, -6, 1]), 2) == 1.0
    assert round(find_zero([1, 2, -3]), 2) == -0.5
    assert round(find_zero([1, -2, 3]), 2) == 0.67
    assert round(find_zero([1, 0]), 2) == 0.0
    assert find_zero([-1]) == 0.0
    assert round(find_zero([-1, 2]), 2) == -0.5
    assert find_zero([]) == 0.0
    assert find_zero([1, 2, 