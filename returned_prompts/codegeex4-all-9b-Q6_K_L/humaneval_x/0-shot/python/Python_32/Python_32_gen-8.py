The provided code has a bug. The `poly` function calculates the polynomial correctly, but the `find_zero` function does not work as expected. It should use the Newton-Raphson method to find the root of the polynomial.

Here's a corrected version of the code:

```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """
    xs are coefficients of a polynomial.
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
    x = 0.0
    while True:
        fx = poly(xs, x)
        fpx = poly([xs[i] * i for i in range(1, len(xs))], x)
        if abs(fx) < 1e-6:
            return x
        x -= fx / fpx


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

In the `find_zero` function, we use the Newton-Raphson method to find the root of the polynomial. The method iteratively improves the guess for the root by taking the average of the root and the value of the polynomial at the current guess. We stop the iterations when the absolute value of the polynomial at the current guess is less than a small threshold (1e-6 in this case).

The `doctest.testmod()` function is used to run the doctests in the code, which are used to verify the correctness