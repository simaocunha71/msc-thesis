    def newton(x_old, f, f_prime):
        x_new = x_old - f(x_old) / f_prime(x_old)
        return x_new

    x_0 = 0
    x_1 = 1

    while abs(x_0 - x_1) > 1e-6:
        x_0 = x_1
        x_1 = newton(x_0, lambda x: poly(xs, x), lambda x: poly(xs, x) / 1)
    return x_1


