    def poly(xs: list, x: float):
        """
        Evaluates polynomial with coefficients xs at point x.
        return xs[0]  xs[1] * x xs[2] * x^2  xs[3] * x^3 .... xs[n] * x^n
        """
        return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

    def f(x):
        """
        return poly(xs, x)
        """
        return poly(xs, x)

    def df(x):
        """
        return derivative of poly(xs, x)
        """
        return sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs)])

    # Use Newton's method to find a root
    x = 0.0
    while True:
        if df(x) == 0:
            # If derivative is zero, then the function is constant
            # and we can't find a root
            return None
        new_x = x - f(x) / df(x)
        if abs(new_x - x) < 0.000001:
            # If the change in x is small, then we've converged to a root
            return new_x
        x = new_x

#Test Cases
print(find_zero([1, 2])) # f(x) = x + 2x^2
print(find_zero([-6, 11, -6, 1])) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(find_zero([1, -5, 6])) # x^2 - 5x + 6
print(find_zero([1, -6, 11, -6])) # (x - 1) * (x - 2) * (x - 3) * (x - 4) = -6 + 11x - 6x^2 + 1x^3
print(find_