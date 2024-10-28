    x_numerator, x_denominator = x.split("/")
    n_numerator, n_denominator = n.split("/")

    result = int(x_numerator) * int(n_denominator) == int(x_denominator) * int(n_numerator)

    return result


