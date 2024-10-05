    def f(x):
        return poly(xs, x)

    def df(x):
        return sum([i * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

    def newton_raphson(x):
        return x - f(x) / df(x)

    x = 0
    while abs(f(x)) > 1e-6:
        x = newton_raphson(x)

    return x


