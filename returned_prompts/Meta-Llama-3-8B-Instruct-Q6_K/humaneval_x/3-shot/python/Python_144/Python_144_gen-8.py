    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    numerator1, denominator1 = map(int, x.split('/'))
    numerator2, denominator2 = map(int, n.split('/'))

    common_denominator = lcm(denominator1, denominator2)
    numerator1 *= common_denominator // denominator1
    numerator2 *= common_denominator // denominator2

    return numerator1 == numerator2


