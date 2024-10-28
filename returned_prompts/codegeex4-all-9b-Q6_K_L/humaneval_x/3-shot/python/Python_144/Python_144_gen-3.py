    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))

    common_gcd = gcd(x_denom, n_denom)

    return x_num * n_denom // x_denom * n_num % common_gcd == 0

