    for i := 1; i < len(xs); i++  {
        if xs[i] != 0  {
            for j := 0; j < len(xs); j++  {
                xs[j] += xs[i] * int(math.Pow(-1, float64(j+i)))
            }
            goto A
        }
    }
    return float64(xs[0]) / float64(xs[1])
}
```

This is a Python solution:

```python
import math

# Evaluates polynomial with coefficients xs at point x.
def poly(xs, x):
    return sum(coeff * x**i for i, coeff in enumerate(xs))

# xs are coefficients of a polynomial.
# FindZero find x such that Poly(x) = 0.
# FindZero returns only only zero point, even if there are many.
# Moreover, FindZero only takes list xs having even number of coefficients
# and largest non zero coefficient as it guarantees
# a solution.
def find_zero(xs):
    n = len(xs)
    if xs[n-1] == 0:
        raise ValueError("The last coefficient cannot be zero.")
    if xs[n-2] == 0:
        return -xs[n-1]/xs[n-2]
    x = -xs[n-1]/xs[n-2]
    while True:
        y = poly(xs, x)
        if abs(y) < 1e-6:
            return x
        x -= y / poly(xs, x +1e-6 if x > 0 else x - 1e-6)
```

This Python solution uses Newton's method to find the roots of the polynomial. It starts with an initial guess and iteratively refines this guess until the function value is close to zero. The derivative of the function is used to estimate the next guess. The derivative is approximated by computing the function value at a very small increment from the current guess.

The Python solution also includes error checking to ensure that the list of coefficients does not end in zero, as this would cause division by zero when computing the initial guess.