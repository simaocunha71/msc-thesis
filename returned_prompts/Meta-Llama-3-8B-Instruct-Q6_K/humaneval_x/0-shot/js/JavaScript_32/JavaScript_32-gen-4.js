Here is the Python solution for the problem:

```Python
import numpy as np

def poly(xs, x):
    return np.polyval(xs, x)

def findZero(xs):
    if len(xs) % 2 == 1:
        raise ValueError("xs must have an even number of coefficients")
    if abs(xs[0]) < 1e-10:
        raise ValueError("xs must have the largest non zero coefficient as the first one")
    return -xs[1]/xs[0]
```

In this code, the `poly` function evaluates the polynomial at a given point. The `findZero` function finds the zero of the polynomial by solving the equation `xs[0] + xs[1] * x + xs[2] * x^2 + ... xs[n] * x^n = 0`. It assumes that the largest non-zero coefficient is the first one and the polynomial has an even number of coefficients. If these conditions are not met, it raises an error. The zero is calculated as `-xs[1]/xs[0]`, which is the root of the linear part of the polynomial.

The numpy library is used for polynomial evaluation. The `polyval` function evaluates a polynomial at a given point. The polynomial is represented as a list of coefficients, where the first coefficient is the constant term, the second coefficient is the coefficient of x, and so on. The `polyval` function uses these coefficients to calculate the value of the polynomial at the given point. 

The `findZero` function is a simple linear equation solver. It calculates the zero of the polynomial by solving the equation `xs[0] + xs[1] * x + xs[2] * x^2 + ... xs[n] * x^n = 0`. The zero is calculated as `-xs[1]/xs[0]`, which is the root of the linear part of the polynomial. This is a simple and efficient way to solve this problem. 

Please note that this function assumes that the polynomial has a single real root. If the polynomial has multiple real roots or complex roots, this function will only find one of them. If the polynomial has no real roots, this function will raise a ZeroDivisionError. 

Also, please note that this function is not robust and may not work correctly for all inputs. For example, if the input is `[0, 0, 0, 0, 0]`, the function will raise a ZeroDivisionError. You