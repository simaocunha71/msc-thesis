The provided solution is mostly correct, but it has a few issues. Here's a corrected version:

```python
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * (x ** i) for i, coeff in enumerate(xs)])


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
    # Check if the number of coefficients is odd
    if len(xs) % 2 != 0:
        raise ValueError("Number of coefficients must be even")

    # Check if the largest non-zero coefficient is positive
    if max(xs) <= 0:
        raise ValueError("Largest non-zero coefficient must be positive")

    # Find the root
    for x in range(-1000, 1000):
        if round(poly(xs, x), 5) == 0:
            return x

    raise RuntimeError("No root found")


print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```

Changes made:

1. Corrected the poly function to use `(x ** i)` instead of `(x ^ i)`.
2. Added a check in the find_zero function