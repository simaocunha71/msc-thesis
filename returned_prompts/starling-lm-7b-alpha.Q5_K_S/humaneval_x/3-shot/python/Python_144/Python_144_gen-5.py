    def gcd(x, y):
        """Return the greatest common divisor of x and y.

        >>> gcd(36, 84)
        12
        """
        while y:
            x, y = y, x % y
        return x

    def simplify(numerator_str, denominator_str):
        numerator = int(numerator_str)
        denominator = int(denominator_str)
        g = gcd(numerator, denominator)
        return gcd(numerator // g, denominator // g) == 1

    return simplify(x, n)


