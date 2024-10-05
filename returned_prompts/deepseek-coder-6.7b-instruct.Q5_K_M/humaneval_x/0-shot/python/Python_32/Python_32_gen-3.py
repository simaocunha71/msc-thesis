Sure, I can help with that. Here's a possible implementation of the `find_zero` function using the bisection method:

```python
def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2)  # f(x) = 𝑥0 𝑥 1
    1.5
    >>> round(find_zero([-6, 11, -6, 1]), 2)  # f(x) = -6 + 𝑥0 𝑥 1 - 𝑥0 𝑥 2 + 𝑥0 𝑥 3
    1.0
    """
    lower = -1000
    upper = 1000
    epsilon = 0.000001

    while True:
        mid = (lower + upper) / 2
        if abs(poly(xs, mid)) < epsilon:
            return mid
        elif poly(xs, lower) * poly(xs, mid) < 0:
            upper = mid
        else:
            lower = mid
```

In this code, the `find_zero` function uses the bisection method to find a root of the polynomial. The bisection method works by repeatedly dividing the interval containing the root in half until the interval is small enough.

Please note that the `find_zero` function assumes that the polynomial has at least one root in the interval [-1000, 1000]. If the polynomial has roots outside this interval, you may need to adjust the initial values of `lower` and `upper`.

Also, the `find_zero` function assumes that the polynomial has at least one root. If the polynomial is constant or all roots are complex, the function will not terminate.

Finally, the `find_zero` function