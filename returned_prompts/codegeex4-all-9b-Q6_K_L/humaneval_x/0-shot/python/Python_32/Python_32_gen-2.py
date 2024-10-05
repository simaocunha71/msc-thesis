The function `find_zero` is supposed to find a zero of a polynomial with coefficients given in the list `xs`. However, the implementation is incorrect and does not work as expected. 

The function `poly` is used to calculate the value of the polynomial at a given point `x`. The function `find_zero` should use an iterative method such as Newton's method or the bisection method to find a zero of the polynomial. 

Here is a corrected implementation of `find_zero` using the bisection method:

```python
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
    """
    a = -100
    b = 100
    while True:
        c = (a + b) / 2
        f_a = poly(xs, a)
        f_c = poly(xs, c)
        if abs(f_c) < 1e-6:
            return c
        elif f_a * f_c < 0:
            b = c
        else:
            a = c
```

In this implementation, we start by choosing an interval `[a, b]` that contains a zero of the polynomial. We then repeatedly bisect the interval and evaluate the polynomial at the midpoint until we find a zero within a tolerance of `1e-6`.