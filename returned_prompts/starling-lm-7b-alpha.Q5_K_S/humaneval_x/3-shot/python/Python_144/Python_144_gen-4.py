    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def simplify_fraction(numerator: int, denominator: int) -> tuple:
        gcd_val = gcd(numerator, denominator)
        return numerator // gcd_val, denominator // gcd_val

    x_num, x_den = simplify_fraction(int(x.split('/')[0]), int(x.split('/')[1]))
    n_num, n_den = simplify_fraction(int(n.split('/')[0]), int(n.split('/')[1]))

    numerator = n_num * x_num
    denominator = x_den * n_den

    gcd_val = gcd(numerator, denominator)
    return numerator // gcd_val, denominator // gcd_val


