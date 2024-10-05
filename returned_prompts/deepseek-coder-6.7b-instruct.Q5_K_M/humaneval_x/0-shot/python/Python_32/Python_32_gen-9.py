The function `find_zero` should use the bisection method to find the roots of the polynomial. The bisection method is a root-finding method that applies to any continuous function for which one knows two values with opposite signs.

Here is the code:

```python
def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    assert len(xs) % 2 == 0, 'Coefficient list must have even length'
    assert xs[0] != 0, 'Coefficient of x^0 must not be zero'

    def poly(x):
        return sum(coeff * x ** i for i, coeff in enumerate(xs))

    a, b = -1, 1  # initial guesses
    while poly(a) * poly(b) >= 0:
        a, b = b, b + 1

    epsilon = 1e-6
    while abs(a - b) > epsilon:
        c = (a + b) / 2
        if poly(c) == 0:
            return c
        elif poly(a) * poly(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
```

The bisection method starts with an interval [a, b] such that f(a)f(b) < 0 and then iteratively refines the interval to contain the root. The interval [a