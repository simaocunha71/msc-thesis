    coeffs_len = len(xs) // 2
    x_powers = range(coeffs_len)
    coefficients = [coeff for coeff in xs[coeffs_len:]]

    for i, x_power in enumerate(x_powers):
        coeff = coefficients[i]
        if coeff == 0:
            continue
        else:
            break

    x_power = x_power + 1
    denominator = coeff * x_power
    numerator = -sum(coefficients[i] * x_power ** i for i in range(coeffs_len))
    x = numerator / denominator

    return round(x, 2)


