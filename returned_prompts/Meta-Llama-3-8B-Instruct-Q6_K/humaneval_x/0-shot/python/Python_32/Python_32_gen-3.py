Here is the solution:

```python
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 != 0:
        raise ValueError("List xs must have even number of coefficients")

    if max([abs(coeff) for coeff in xs]) == 0:
        raise ValueError("List xs must have at least one non zero coefficient")

    def poly_derivative(xs):
        return [i * coeff for i, coeff in enumerate(xs) if i > 0]

    def newton_raphson(x0):
        for _ in range(100):
            x1 = x0 - poly(xs, x0) / poly_derivative(xs, x0)
            if abs(x1 - x0) < 1e-6:
                return round(x1, 2)
            x0 = x1
        raise ValueError("Newton-Raphson method failed to find a root")

    return newton_raphson(1)
```

This solution uses the Newton-Raphson method to find the root of the polynomial. The Newton-Raphson method is an iterative method that starts with an initial guess for the root and then updates the guess based on the value of the polynomial and its derivative at the current guess. The method is guaranteed to converge to a root if the initial guess is close enough