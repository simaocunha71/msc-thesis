    coeff = xs[::-1]
    return (-coeff[1] + math.sqrt(coeff[1] ** 2 - 4 * coeff[0] * coeff[2])) / (2 * coeff[2])


