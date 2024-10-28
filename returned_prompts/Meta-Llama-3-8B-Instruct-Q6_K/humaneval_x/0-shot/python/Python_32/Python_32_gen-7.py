Here is the solution in Python:

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
        raise ValueError("Number of coefficients must be even")

    largest_coeff = max([abs(coeff) for coeff in xs])
    for x in [i/10.0 for i in range(-100, 101)]:
        if abs(poly(xs, x)) < 1e-6 and abs(xs[0]) == largest_coeff:
            return round(x, 2)
    return None
```
This code defines two functions: `poly` to evaluate a polynomial at a point, and `find_zero` to find a root of a polynomial. The `find_zero` function iterates over a range of x values and checks if the polynomial is close to zero. It returns the first x value that it finds that satisfies this condition. If no such x value is found, it returns None. The function also checks that the input list has an even number of coefficients. If it does not, it raises a ValueError. The function also checks that the largest coefficient is non-zero, as a polynomial with only zero coefficients has no roots. If the largest coefficient is zero, the function returns None. The function uses the `round` function to round the result to two