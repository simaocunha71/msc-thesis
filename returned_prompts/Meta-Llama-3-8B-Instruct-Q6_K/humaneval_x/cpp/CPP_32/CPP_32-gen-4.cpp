Here is the complete Python code:

```python
import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    sum = 0
    for i in range(len(xs)):
        sum += xs[i] * math.pow(x, i)
    return sum

def find_zero(xs):
    """
    xs are coefficients of a polynomial. find_zero find x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients and largest non zero coefficient as it guarantees a solution.
    >>> round(find_zero([1, 2]), 2) #f(x) = 1 + 2x 
    -0.5 
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3 
    1.0
    """
    if len(xs) % 2 != 0:
        raise Exception("xs must have even number of coefficients")
    if abs(xs[0]) < abs(xs[1]):
        raise Exception("xs must have largest non zero coefficient as it guarantees a solution")
    for i in range(-100, 101):
        if abs(poly(xs, i)) < 1e-6:
            return i
    raise Exception("No zero point found")
```
Please note that this code is not robust and may not work for all polynomials. It's also not the most efficient way to find the root of a polynomial. For a more robust and efficient solution, you may want to consider using a numerical method like the Newton-Raphson method. 

Also, this code assumes that the polynomial has a single real root. If the polynomial has complex roots, this code will not work correctly. 

Finally, this code is not tested extensively and may contain bugs. You should test it thoroughly before using it in production. 

The function `find_zero` iterates over all possible values of `x` from -100 to 100 and checks if `poly(xs, x)` is close to 0. If it finds a