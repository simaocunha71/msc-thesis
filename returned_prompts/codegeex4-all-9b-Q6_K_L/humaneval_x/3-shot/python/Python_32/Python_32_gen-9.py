    def f(x):
        return poly(xs, x)

    def f_prime(x):
        return poly([i * xs[i] for i in range(len(xs) - 1)], x)

    def newton_raphson(x):
        return x - f(x) / f_prime(x)

    x = 0.0
    while abs(f(x)) > 1e-6:
        x = newton_raphson(x)

    return x


