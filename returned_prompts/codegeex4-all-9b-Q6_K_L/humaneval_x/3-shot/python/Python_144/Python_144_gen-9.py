    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))

    gcd_value = gcd(numerator_x, denominator_n)
    lcm_value = lcm(denominator_x, denominator_n)

    return (numerator_x * denominator_n) // gcd_value == (numerator_n * denominator_x) // gcd_value

