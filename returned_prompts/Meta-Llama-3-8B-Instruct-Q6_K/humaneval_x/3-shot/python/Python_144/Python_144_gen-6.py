    def lcm(a, b):
        return (a * b) // math.gcd(a, b)

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x_numerator, x_denominator = map(int, x.split('/'))
    n_numerator, n_denominator = map(int, n.split('/'))

    common_denominator = lcm(x_denominator, n_denominator)
    x_numerator *= common_denominator // x_denominator
    n_numerator *= common_denominator // n_denominator

    return x_numerator * n_numerator == common_denominator
# Solution ends here


