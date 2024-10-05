To solve this problem we can use Newton's method, also known as the Newton–Raphson method, a root-finding algorithm which produces successively better approximations to the zeroes of a real-valued function.

Here is the step-by-step process of Newton's method:

1. We start with a guess x₀. This is usually the average of the two endpoints of the interval.
2. Then, we calculate the next approximation as follows: x₁ = x₀ - f(x₀) / f'(x₀)
3. We repeat step 2 until we reach the desired accuracy.

Here is the Python implementation of Newton's method:

```python
def newton(f, df, x0, tol=1e-6, max_iter=100):
    """ Implement Newton's method """
    x = x0
    for i in range(max_iter):
        if abs(f(x)) < tol:
            return x
        x -= f(x) / df(x)
    return x
```

Here is the Python implementation of the `findZero` function:

```python
def findZero(xs):
    # Make sure xs has even number of coefficients
    assert len(xs) % 2 == 0
    # Find the largest non zero coefficient
    c = 0
    while c < len(xs) and xs[c] == 0:
        c += 1
    # Define the function f(x) = sum(xs[i] * x^i)
    def f(x):
        s = 0
        for i in range(c, len(xs)):
            s += xs[i] * x**i
        return s
    # Define the derivative of f(x)
    def df(x):
        s = 0
        for i in range(c+1, len(xs)):
            s += xs[i] * (i+1) * x**i
        return s
    # Start with the average of the two endpoints of the interval
    x0 = (1 + xs[-1]/xs[0]) / 2
    # Run Newton