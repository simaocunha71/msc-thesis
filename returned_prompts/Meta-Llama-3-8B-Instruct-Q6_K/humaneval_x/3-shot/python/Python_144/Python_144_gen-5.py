    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_fraction(frac):
        numerator, denominator = map(int, frac.split('/'))
        common_divisor = gcd(numerator, denominator)
        return str(numerator // common_divisor) + '/' + str(denominator // common_divisor)

    x = simplify_fraction(x)
    n = simplify_fraction(n)

    return x == n
