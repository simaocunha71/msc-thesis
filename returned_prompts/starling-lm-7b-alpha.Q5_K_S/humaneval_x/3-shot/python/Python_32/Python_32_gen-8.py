    coeffs = [coeff / abs(coeff) for coeff in xs]
    x = -coeffs[1] / coeffs[0]
    return x


