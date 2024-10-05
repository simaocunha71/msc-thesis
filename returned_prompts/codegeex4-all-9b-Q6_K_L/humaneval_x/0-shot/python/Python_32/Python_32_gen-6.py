Your implementation of the find_zero function seems correct. It takes a list of coefficients, xs, and uses the poly function to evaluate the polynomial at various points until it finds a zero. 

The function starts by checking if the length of the list is odd. If it is, it raises a ValueError. This is because a polynomial with an odd number of coefficients can have more than one real zero, which makes finding a specific zero ambiguous.

Next, it defines a step size based on the number of coefficients. The step size is calculated by taking the absolute value of the maximum coefficient in the list and dividing it by the square root of the number of coefficients.

Then, it iterates over a range of values starting from -1 and ending at 1 (inclusive), with a step size. For each value, it evaluates the polynomial using the poly function and checks if the result is close enough to zero (within a tolerance of 1e-10). If it is, it returns the current value as the zero.

If the function doesn't find a zero after the loop, it raises a ValueError. This indicates that there may not be a zero within the range of values tested, or that the polynomial may not have a real zero.

Here's the code again for reference:

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
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
   