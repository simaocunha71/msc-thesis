    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    common_divisor = gcd(x_den, n_den)

    return (x_num * n_den) % common_divisor == 0 and (n_num * x_den) % common_divisor == 0

