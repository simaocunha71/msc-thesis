To find a zero of a polynomial, you need to use Newton's method.

Here are the steps:

1. Set the initial guess to be zero. That is,
   x0 = 0.
2. Use the formula
     x_k+1 = x_k - f(x_k) / f'(x_k)
   to update the guess. Here, f(x) is the value of the polynomial at x,
   and f'(x) is the derivative of the polynomial at x.
3. Repeat step 2 until the guess converges.

The formula in step 2 is Newton's method.

Here is a Python function that implements Newton's method for finding a zero of a polynomial:

```python
def newton(f, df, x0=0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        if abs(f(x)) < tol:
            return x
        x -= f(x) / df(x)
    return x
```

Here is an implementation of the `findZero` function:

```python
from math import pow
from sympy import symbols, diff

def findZero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    x = symbols('x')
    f = lambda x: poly(xs, x)
    df = lambda x: sum(xs[i] * pow(x, i) * (i + 1) for i in range(len(xs)))
    return newton(f, df)
```

Note: The `findZero` function requires the `sympy` library. You can install it using `pip install sympy`.

Here are some test cases for the `findZero` function:

```python
print(round(findZero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(findZero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x