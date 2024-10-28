    def f(x):
        return poly(xs, x)

    def df(x):
        n = len(xs)
        return sum([i * xs[i] * math.pow(x, i - 1) for i in range(1, n)])

    x = 0.0
    while abs(f(x)) > 1e-6:
        x = x - f(x) / df(x)

    return x


