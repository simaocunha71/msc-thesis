    if len(xs) % 2 != 0:
        return ValueError("xs must have even number of coefficients")
    # get largest non zero coefficient
    sign = 1 if xs[0] >= 0 else -1
    xs = [abs(x) for x in xs]
    for i in range(1, len(xs)):
        if xs[i] > xs[i - 1]:
            sign = 1
        elif xs[i] < xs[i - 1]:
            sign = -1
        xs[i] = abs(xs[i])
    # find zero point using Bisection method
    a, b = -1000, 1000
    while True:
        x = (a + b) / 2
        if abs(poly(xs, x)) < 0.00001:
            return round(x, 2) * sign
        elif poly(xs, a) * poly(xs, b) < 0:
            b = x
        else:
            a = x


# Made By Mostafa_Khaled
```
1
2
3
```
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
    >>> round(find_