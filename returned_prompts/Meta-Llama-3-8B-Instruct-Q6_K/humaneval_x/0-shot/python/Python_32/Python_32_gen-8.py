Here is the Python code for the problem. It uses the Newton-Raphson method to find the root of the polynomial. The method starts with an initial guess for the root and iteratively refines the guess until it converges.

```Python
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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """

    def derivative(xs: list, x: float):
        """
        Compute the derivative of the polynomial at point x.
        """
        return sum([i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs)])

    def newton_raphson(xs: list, x0: float):
        """
        Find the root of the polynomial using Newton-Raphson method.
        """
        while True:
            x1 = x0 - poly(xs, x0) / derivative(xs, x0)
            if abs(x1 - x0) < 1e-6:
                return x1
            x0 = x1

    # Check if the input list has even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("List xs must have even number of coefficients")

    # Find the largest non-zero coefficient
    max_coeff = max([coeff for coeff in xs if coeff != 0])

    # Start with an initial guess for the root
