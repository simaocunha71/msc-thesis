
I'm not sure what you're trying to do here. The function `poly` takes two arguments, a list of coefficients and a value to evaluate the polynomial at. The function `find_zero` should find the value of `x` that makes the polynomial equal to zero. The derivative of a polynomial is a new polynomial, so the function `derivative` takes a list of coefficients and returns a new list of coefficients. The function `find_zero` should find the value of `x` that makes the derivative of the polynomial equal to zero. The function `find_zero` should return the value of `x` that makes the polynomial equal to zero. The function `find_zero` should return the value of `x` that makes the derivative of the polynomial equal to zero.
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
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 +