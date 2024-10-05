Sure, here is a Python code to solve the problem:

```python
def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1]  * x + xs[2]  * x^2 + .... xs[n]  * x^n
    """
    return sum([coeff * x**i for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x  - 1) * (x  - 2) * (x  - 3) = -6 + 11x - 6x^2 +  x^3
    1.0
    """
    # Bisection method
    a, b = -1000, 1000  # initial guesses
    while abs(poly(xs, a)) > pow(10, -8):
        c = (a + b) / 2
        if poly(xs, a) * poly(xs, c) <= 0:
            b = c
        else:
            a = c
    return a
```
The function find_zero uses the bisection method to find a root of a polynomial. The initial guesses for the roots are chosen as -1000 and 1000. The while loop continues until the absolute value of the polynomial evaluated at a is less than 10^-8. The function poly evaluates the polynomial at a point x.

The bisection method is a root-finding method that applies to any continuous functions for which one