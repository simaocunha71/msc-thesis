    from fractions import Fraction

    x = Fraction(x)
    n = Fraction(n)

    return (x * n).limit_denominator() == x * n

