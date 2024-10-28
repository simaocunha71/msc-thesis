    def poly_diff(xs):
        return [i * xs[i] for i in range(1, len(xs))]

    def newton_raphson(f, df, x0):
        epsilon = 0.00001
        while True:
            x1 = x0 - f(x0) / df(x0)
            if abs(x1 - x0) < epsilon:
                return x1
            x0 = x1

    return newton_raphson(lambda x: poly(xs, x), lambda x: poly(poly_diff(xs), x), 0.0)


