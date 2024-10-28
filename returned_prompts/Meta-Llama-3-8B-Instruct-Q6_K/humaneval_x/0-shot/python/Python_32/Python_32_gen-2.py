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
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the number of coefficients is even
    if len(xs) % 2 == 1:
        raise ValueError("The number of coefficients must be even")

    # Check if the largest non zero coefficient is not 0
    if max([coeff for coeff in xs if coeff != 0]) == 0:
        raise ValueError("The largest non zero coefficient must not be 0")

    # Initialize the initial guess
    x0 = 1

    # Define the tolerance for the root finding
    tol = 1e-6

    # Perform the Newton-Raphson method
    while True:
        # Compute the value of the polynomial at x0
        f0 = poly(xs, x0)
        # Compute the derivative of the polynomial at x0
        df0 = poly([i * coeff for i, coeff in enumerate(xs) if i > 0], x0)
        # Compute the next guess
        x1 = x0 - f0 / df0
        # Check if the tolerance is reached
        if abs(x1 - x0) < tol:
            return round(x1, 2)
        # Update the guess
        x0 = x1
``