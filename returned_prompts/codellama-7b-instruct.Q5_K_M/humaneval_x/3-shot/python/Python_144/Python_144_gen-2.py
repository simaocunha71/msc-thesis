    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')

    x_numerator = int(x_numerator)
    x_denominator = int(x_denominator)

    n_numerator = int(n_numerator)
    n_denominator = int(n_denominator)

    return x_numerator * n_denominator == x_denominator * n_numerator


