    from fractions import Fraction

    return Fraction(x) * Fraction(n) == Fraction(x) * Fraction(n).limit_denominator()