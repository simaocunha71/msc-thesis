    # Find the largest coefficient
    max_coeff = max(xs)

    # Find the index of the largest coefficient
    max_coeff_index = xs.index(max_coeff)

    # If the index is odd, swap the coefficients at indices max_coeff_index and max_coeff_index + 1
    if max_coeff_index % 2 == 1:
        xs[max_coeff_index], xs[max_coeff_index + 1] = xs[max_coeff_index + 1], xs[max_coeff_index]

    # Calculate the polynomial at x = 0
    poly_at_0 = poly(xs, 0)

    # Return the zero point
    return -poly_at_0 / max_coeff

