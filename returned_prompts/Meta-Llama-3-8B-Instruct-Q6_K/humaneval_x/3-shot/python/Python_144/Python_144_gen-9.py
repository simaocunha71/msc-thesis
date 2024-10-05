    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    common_den = lcm(x_den, n_den)
    x_num *= common_den // x_den
    n_num *= common_den // n_den

    if x_num % n_num == 0:
        return True
    else:
        return False


