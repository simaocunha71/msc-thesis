Here is a Python function that will find the zero of a polynomial. This function uses the Newton-Raphson method to find the zero. The Newton-Raphson method is an iterative method that is used to find the roots of a function.

```python
import numpy as np

def poly(xs, x):
    return np.polyval(xs, x)

def find_zero(xs):
    # Check if the degree of the polynomial is even
    if len(xs) % 2 == 1:
        raise ValueError("Polynomial must have an even number of coefficients")

    # Check if the largest coefficient is zero
    if abs(xs[0]) < 1e-6:
        raise ValueError("Polynomial must have a non-zero constant term")

    # Initialize the initial guess for the root
    x0 = 1.0

    # Iterate until the root is found
    while True:
        x1 = x0 - poly(xs, x0) / poly([i * x for i in xs], x0)
        if np.isclose(poly(xs, x1), 0):
            return x1
        x0 = x1
```

This function first checks if the polynomial has an even number of coefficients and if the largest coefficient is zero. Then it initializes the initial guess for the root and iterates until the root is found. The Newton-Raphson method is used to find the root in each iteration.

You can use this function to find the zero of a polynomial as follows:

```python
xs = [1, 2]  # coefficients of the polynomial
x = find_zero(xs)
print(x)  # prints the zero of the polynomial
```

This will find the zero of the polynomial f(x) = 1 + 2x. You can replace the coefficients in the list xs with the coefficients of the polynomial you want to find the zero of.