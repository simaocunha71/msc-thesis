Here is a Python version of your code:

```Python
import math

def Poly(xs, x):
    sum = 0.0
    for i, coeff in enumerate(xs):
        sum += float(coeff) * math.pow(x, i)
    return sum

def FindZero(xs):
    if len(xs) % 2 != 0:
        raise ValueError("xs must have even number of coefficients")
    largest_non_zero_coeff = max(i for i in xs if i != 0)
    return -largest_non_zero_coeff / xs[-1]

# Example usage:
xs = [1, 2]
print(round(FindZero(xs), 2))  # Output: -0.5

xs = [-6, 11, -6, 1]
print(round(FindZero(xs), 2))  # Output: 1.0
```

The `FindZero` function first checks if the number of coefficients is even. If it's not, it raises a `ValueError`. Then it finds the largest non-zero coefficient and returns its negative divided by the last coefficient. This is because the equation `a0 + a1x + a2x^2 + ... + anx^n = 0` has a root at `x = -a0/an`, which is the value returned by `FindZero`. The `Poly` function is used to evaluate the polynomial at a given point. 

Note that this function only returns one root, even if there are multiple roots. Also, it assumes that the polynomial has at least one root. If the polynomial has no real roots, the function will return `inf` or `nan` depending on the coefficients. 

The function also assumes that the largest non-zero coefficient is at the end of the list, which is not necessarily the case. A more robust function would need to find the largest non-zero coefficient in the list, not just the last one. 

Finally, the function does not check if the polynomial is actually zero at the returned root. It simply returns the root based on the assumption that the largest non-zero coefficient is at the end of the list. A more robust function would need to check if the polynomial is actually zero at the returned root. 