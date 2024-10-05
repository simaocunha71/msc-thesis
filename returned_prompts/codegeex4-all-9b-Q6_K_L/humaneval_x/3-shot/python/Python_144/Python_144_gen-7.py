    def gcd(a, b):
        """Compute the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    numerator = int(x.split('/')[0])
    denominator = int(x.split('/')[1])

    numerator *= int(n.split('/')[1])
    denominator *= int(n.split('/')[0])

    common_divisor = gcd(numerator, denominator)

    return numerator // common_divisor == denominator // common_divisor

    # return eval(x) * eval(n) == int(eval(x) * eval(n))

