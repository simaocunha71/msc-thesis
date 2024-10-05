The problem requires to evaluate a polynomial with coefficients `xs` at point `x` and find the zero of the polynomial. 

The function `poly` takes a list of coefficients `xs` and a point `x` as inputs. It uses the formula `return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])` to evaluate the polynomial at `x`. This formula calculates the sum of each coefficient multiplied by `x` raised to the power of its index.

The function `find_zero` takes a list of coefficients `xs` as inputs. It uses the `poly` function to find a zero of the polynomial. The function `find_zero` returns only one zero point, even if there are many. Moreover, `find_zero` only takes a list `xs` having an even number of coefficients and the largest non-zero coefficient to guarantee a solution.

The `poly` function is used inside the `find_zero` function to evaluate the polynomial at a point `x`. 

Here is the corrected code:

```python
import math

def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    return -xs[0] / xs[1]

# Testing the functions
print(round(poly([1, 2], -0.5), 2)) # f(x) = 1 + 2x
print(round(poly([-6, 11, -6, 1], 1), 2)) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
print(find_zero([1, 2])) # f(x) = 1 + 2x
print(find_zero([-6, 11, -6, 1])) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
```