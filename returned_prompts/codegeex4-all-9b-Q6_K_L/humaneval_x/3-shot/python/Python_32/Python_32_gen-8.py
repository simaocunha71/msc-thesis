    # first, we need to find the largest non zero coefficient
    max_coeff = max(xs)
    max_coeff_idx = xs.index(max_coeff)

    # then, we need to find the zero point
    zero_point = 0.0
    while poly(xs, zero_point) != 0:
        zero_point += 0.0001

    return zero_point


