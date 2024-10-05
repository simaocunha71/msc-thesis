    import fractions
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    x_frac = fractions.Fraction(x_num, x_den)
    n_frac = fractions.Fraction(n_num, n_den)
    return (x_frac * n_frac).denominator == 1

