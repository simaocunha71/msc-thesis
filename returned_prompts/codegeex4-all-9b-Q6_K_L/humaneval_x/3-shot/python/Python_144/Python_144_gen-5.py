    from fractions import Fraction

    frac_x = Fraction(x)
    frac_n = Fraction(n)

    return frac_x * frac_n == frac_x * frac_n.as_integer_ratio()[1] // frac_n.as_integer_ratio()[0]

