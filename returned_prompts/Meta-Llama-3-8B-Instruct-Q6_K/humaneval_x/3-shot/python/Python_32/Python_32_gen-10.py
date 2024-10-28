    if len(xs) % 2 == 0 and abs(xs[0]) > abs(xs[-1]):
        return -xs[1] / xs[2]
    else:
        raise ValueError("Invalid input for find_zero function")
    # The idea here is that the largest non-zero coefficient (usually the constant term) is at index 0
    # and the coefficient of the linear term is at index 1. The zero point is then the negative of the coefficient of the linear term divided by the coefficient of the quadratic term.
    # This works because the polynomial is a quadratic, and the quadratic formula is not needed for this simple case. If you need to find the roots of a more complex polynomial, you would need to use a more sophisticated method.