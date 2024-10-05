Here is a Python version of the code:

```Python
def poly(xs, x):
    return sum([xi * x**i for i, xi in enumerate(reversed(xs))])

def findZero(xs):
    if len(xs) % 2 == 1:
        raise ValueError("xs must have an even number of coefficients")

    max_coefficient = max(abs(xi) for xi in xs)
    max_coefficient_index = xs.index(max_coefficient)

    return round(-xs[max_coefficient_index] / xs[max_coefficient_index + 1], 2)
```

In the `findZero` function, we first check if the number of coefficients is even. If not, we raise a `ValueError`. Then we find the index of the maximum absolute value coefficient. The zero of the polynomial is the negative of this coefficient divided by the coefficient at the next index. We round the result to 2 decimal places. 

Note: This function assumes that the polynomial has a unique real root and that the coefficient at the next index is non-zero. If the polynomial has more than one real root or if the coefficient at the next index is zero, this function will not work correctly. 

Also, the `poly` function is a helper function that calculates the value of the polynomial at a given point. It uses a list comprehension to sum the products of each coefficient and the corresponding power of `x`. The `enumerate` function is used to get both the index and the value of each coefficient. The `reversed` function is used to iterate over the coefficients in reverse order, so that the first coefficient is the constant term and the last coefficient is the term with the highest power of `x`.  The `sum` function is used to calculate the sum of the products.  This function is used by the `findZero` function to calculate the value of the polynomial at the zero. 