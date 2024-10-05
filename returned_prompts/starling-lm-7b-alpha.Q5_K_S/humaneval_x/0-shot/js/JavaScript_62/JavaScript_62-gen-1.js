The derivative of a polynomial is a polynomial of one order less, obtained by differentiating all the terms. The derivative of x^n is n * x^(n-1). So,

    The derivative of x is 1,
    The derivative of x^2 is 2 * x,
    The derivative of x^3 is 3 * x^2,
    ...

Here's one way to implement this in Python:

```python
def derivative(xs):
    result = []
    for i in range(1, len(xs)):
        result.append(xs[i] * i)
    return result
```

This will work for any list of coefficients, not just polynomials. For example, `derivative([3, 1, 2, 4, 5])` returns `[1, 4, 12, 20]` and `derivative([1, 2, 3])` returns `[2, 6]`.

This code works by iterating over each term in the polynomial (starting at index 1, since the derivative of the constant term is 0). For each term, it multiplies the coefficient by the exponent (which is `i`), and appends the result to the `result` list.

Note that the `range(1, len(xs))` generates a sequence of numbers from 1 to the length of the input list (exclusive), which corresponds to the exponents of the terms in the polynomial.

The function returns the `result` list, which contains the derivatives of the original polynomial.

Here's an example usage:

```python
print(derivative([3, 1, 2, 4, 5]))  # prints: [1, 4, 12, 20]
print(derivative([1, 2, 3]))  # prints: [2, 6]
```

In the first example, the derivative of `3 + x + 2x^2 + 4x^3 + 5x^4` is `1 + 4x + 6x^2 + 12x^3`. In the second example, the derivative of `1 + 2x + 3x^