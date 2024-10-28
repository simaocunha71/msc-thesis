    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(frac):
        numerator, denominator = map(int, frac.split('/'))
        common_divisor = gcd(numerator, denominator)
        return str(numerator // common_divisor) + '/' + str(denominator // common_divisor)

    x_simplified = simplify_fraction(x)
    n_simplified = simplify_fraction(n)

    x_numerator, x_denominator = map(int, x_simplified.split('/'))
    n_numerator, n_denominator = map(int, n_simplified.split('/'))

    return x_numerator * n_denominator == x_denominator * n_numerator


