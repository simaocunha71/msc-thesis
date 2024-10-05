    def f(x):
        return poly(xs, x)

    def df(x):
        h = 0.00001
        return (f(x + h) - f(x)) / h

    x = 0.0
    while abs(f(x)) > 0.0001:
        x = x - f(x) / df(x)

    return x


