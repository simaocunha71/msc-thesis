Here is a Python code snippet that implements the find_zero function. It uses the Newton-Raphson method to find a root of the polynomial.

```Python
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
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    """
    assert len(xs) % 2 == 0, 'xs should have even number of coefficients'
    assert max([abs(coeff) for coeff in xs]) != 0, 'xs should have a non zero coefficient'
    n = len(xs)
    x = 1.0  # initial guess
    for _ in range(100):  # max 100 iterations
        p = poly(xs, x)
        if abs(p) < 1e-6:
            return round(x, 2)
        x = x - p / poly([i * coeff for i, coeff in enumerate(xs)], x)
    return round(x, 2)
```

You can test the function with the following examples:

```Python
print(round(find_zero([1, 2]), 2))  # f(x) = 1 + 2x
print(round(find_zero([-6, 11, -6, 1]), 2))  # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```


This code first ensures that the input list of coefficients has an even number of elements and that the largest non-zero coefficient is non-zero. Then it uses the Newton-Raphson method to iteratively refine an initial guess for the root until the polynomial's value at that point is close enough to zero. The method is stopped after a maximum of 100 iterations. The final result is rounded to two decimal places. The function will return