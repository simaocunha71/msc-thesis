The function `find_zero` is intended to find a zero of a polynomial given its coefficients. However, the function is not implemented yet. We can use the `scipy.optimize.root` function from the `scipy` library to find the roots of a polynomial. Here's how you can implement `find_zero`:

```python
import math
from scipy.optimize import root

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    def f(x):
        return poly(xs, x)
    
    solution = root(f, 0)
    return solution.x[0]
```

In this implementation, we define a helper function `f(x)` which represents the polynomial. Then, we use `root` to find the root of `f(x)` starting from `x = 0`. The `root` function returns a `RootResults` object which contains the root of the polynomial. We return the first element of `solution.x` which is the root of the polynomial.

Now, you can test `find_zero` with the provided examples:

```python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```