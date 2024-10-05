    if len(xs) % 2 == 1:
        raise ValueError("xs should have even number of coefficients.")

    # Find the largest non-zero coefficient
    largest_coeff = max(xs)

    if largest_coeff == 0:
        raise ValueError("xs should have a non-zero coefficient.")

    # Find a zero point
    zero_point = -xs[0] / largest_coeff

    return zero_point

