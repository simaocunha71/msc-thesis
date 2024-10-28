    coeff = [coeff / abs(coeff) for coeff in xs]
    return -poly(coeff, 1 / coeff[0])


