    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_fraction(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        common_divisor = gcd(numerator, denominator)
        return str(numerator // common_divisor) + '/' + str(denominator // common_divisor)

    x = simplify_fraction(x)
    n = simplify_fraction(n)

    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    return x_numerator * n_denominator * n_numerator * x_denominator == x_denominator * n_denominator * x_numerator * n_numerator


