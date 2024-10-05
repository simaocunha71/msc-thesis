    # The function to evaluate
    def f(x):
        return poly(xs, x)

    # The function to evaluate the derivative of the polynomial
    def df(x):
        return poly([i * xs[i] for i in range(1, len(xs))], x)

    # The function to perform one step of Newton's method
    def newton(x):
        return x - f(x) / df(x)

    # The starting point for Newton's method
    x = 0

    # Perform Newton's method until the function value is close to zero
    while abs(f(x)) > 1e-6:
        x = newton(x)

    return x

