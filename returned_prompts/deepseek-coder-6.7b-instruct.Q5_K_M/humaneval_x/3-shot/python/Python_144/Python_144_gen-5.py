    from fractions import Fraction

    f1 = Fraction(int(x.split('/')[0]), int(x.split('/')[1]))
    f2 = Fraction(int(n.split('/')[0]), int(n.split('/')[1]))

    return (f1 * f2).denominator == 1


