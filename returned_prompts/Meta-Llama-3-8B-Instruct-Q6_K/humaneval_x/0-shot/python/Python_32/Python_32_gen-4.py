Here is the corrected version of the code:

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
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    if len(xs) % 2 == 1:
        raise ValueError("xs should have even number of coefficients")
    max_coeff_idx = max(range(len(xs)), key=lambda i: abs(xs[i]))
    return -xs[max_coeff_idx] / xs[max_coeff_idx - 1]
```

The function `find_zero` is updated to handle the case when the input list `xs` has an odd number of coefficients. It also uses the largest non-zero coefficient to find the zero point, as guaranteed by the theorem of polynomial equation. Note that this method is not robust and may not work for all cases, especially when the polynomial has multiple roots. For more robust methods, you may want to consider using numerical methods such as Newton's method or polynomial root finding algorithms.