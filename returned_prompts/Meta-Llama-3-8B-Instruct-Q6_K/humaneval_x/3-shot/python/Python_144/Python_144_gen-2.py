    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(frac):
        numerator, denominator = map(int, frac.split('/'))
        gcd_value = gcd(numerator, denominator)
        return str(numerator // gcd_value) + '/' + str(denominator // gcd_value)

    x = simplify_fraction(x)
    n = simplify_fraction(n)

    return x == n


