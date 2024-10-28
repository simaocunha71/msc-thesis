    # we want to solve f(x) = 0, i.e. f(x) - 0 = 0
    # we can use the Newton-Raphson method to find the zero
    # we start with an initial guess x0
    # and then we iteratively update it using the formula:
    # x_{n+1} = x_n - f(x_n) / f'(x_n)
    # where f'(x) is the derivative of f(x)
    # we stop when |f(x)| < epsilon, where epsilon is a small number
    # such as 1e-6
    epsilon = 1e-6
    x = 0
    while abs(poly(xs, x)) > epsilon:
        x = x - poly(xs, x) / poly(xs, x + epsilon)
    return x

