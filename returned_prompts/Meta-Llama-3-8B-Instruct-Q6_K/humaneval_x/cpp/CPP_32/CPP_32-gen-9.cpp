Here is a simple implementation in Python:

```Python
import numpy as np
from scipy.optimize import root_scalar

def find_zero(xs):
    """
    Find the zero of a polynomial.

    Parameters
    ----------
    xs : list of float
        Coefficients of the polynomial.

    Returns
    -------
    float
        The zero of the polynomial.
    """
    if len(xs) % 2 == 1:
        raise ValueError('Polynomial must have an even number of coefficients.')
    if abs(xs[0]) < 1e-10:
        raise ValueError('Leading coefficient must be non-zero.')
    poly = np.poly1d(xs)
    root = root_scalar(poly, bracket=[-1, 1])
    return root.root
```

This function first checks if the polynomial has an even number of coefficients and if the leading coefficient is non-zero. Then it uses the `root_scalar` function from `scipy.optimize` to find the zero of the polynomial. The `root_scalar` function returns an object that contains information about the root, including the root itself (`root.root`). The function then returns this root.

This function works by using the `root_scalar` function to find the zero of the polynomial. The `root_scalar` function uses a variety of methods to find the root, including the Brent method, the secant method, and the bisection method.

Here is how you can use this function:

```Python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```





