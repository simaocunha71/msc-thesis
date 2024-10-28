    # find the largest non zero coefficient
    max_coeff = max([abs(coeff) for coeff in xs])

    # find the largest index of the largest non zero coefficient
    max_coeff_index = xs.index(max_coeff)

    # find the zero point
    zero_point = -xs[max_coeff_index] / max_coeff

    return zero_point