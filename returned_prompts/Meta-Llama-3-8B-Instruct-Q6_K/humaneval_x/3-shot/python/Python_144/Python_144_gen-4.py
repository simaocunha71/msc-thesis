    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    def simplify_fraction(fraction):
        numerator, denominator = map(int, fraction.split('/'))
        common_divisor = gcd(numerator, denominator)
        return str(numerator // common_divisor) + '/' + str(denominator // common_divisor)

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    lcm_den = lcm(x_den, n_den)

    simplified_x = simplify_fraction(str(x_num * n_num) + '/' + str(lcm_den))
    return simplified_x == '1/1'  # Return True if the simplified fraction is 1/1, False otherwise
