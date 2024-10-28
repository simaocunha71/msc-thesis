    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    if (n_numerator * x_denominator) % x_numerator == 0:
        return True
    else:
        return False


