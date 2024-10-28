    import fractions

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    x = fractions.Fraction(x_num, x_den)
    n = fractions.Fraction(n_num, n_den)

    return (x * n).denominator == 1


