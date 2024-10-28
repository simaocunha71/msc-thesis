    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    common_gcd = gcd(x_den, n_num)
    simplified_x_den = x_den // common_gcd
    simplified_n_num = n_num // common_gcd

    return simplified_x_den * n_den == simplified_n_num