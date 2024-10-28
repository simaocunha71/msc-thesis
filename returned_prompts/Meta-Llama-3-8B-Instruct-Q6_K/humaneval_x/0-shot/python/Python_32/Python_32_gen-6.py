I implemented a function named find_zero that takes a list of coefficients as input. This function returns the zero point of the polynomial. The function assumes that the input list has an even number of coefficients, and the largest non-zero coefficient is guaranteed to have a solution. The function uses the poly function to evaluate the polynomial at different points and find the zero point.

Here's the solution:
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
    # find the largest non-zero coefficient
    max_coeff = max((abs(coeff), i) for i, coeff in enumerate(xs))[1]
    # start from the largest non-zero coefficient
    x0 = 1 - max_coeff
    # use Newton's method to find the zero point
    for _ in range(10):  # run 10 iterations
        x = x0 - poly(xs, x0) / poly([i * c for i, c in enumerate(xs)], x0)
        x0 = x
    return round(x0, 2)
```
Note that the find_zero function uses Newton's method to find the zero point. This method is an iterative process that starts with an initial guess and refines it until it converges to the zero point. In this implementation, I use the largest non-zero coefficient as the initial guess and run the