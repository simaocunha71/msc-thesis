Here is the Python code for the problem:

```python
def Derivative(xs):
    if len(xs) == 0:
        return []
    return [i * xs[i] for i in range(1, len(xs))]
```

The function `Derivative` takes a list of coefficients `xs` as input, where `xs[0] + xs[1] * x + xs[2] * x^2 + ...` is a polynomial. It returns the derivative of this polynomial in the same form.

The function checks if the input list is empty. If it is, it returns an empty list.

Otherwise, it uses a list comprehension to calculate the derivative. The derivative of a polynomial is obtained by multiplying each coefficient by its corresponding power of `x`, and then decrementing the power by 1. Therefore, the function iterates over the range `1` to `len(xs)-1` (inclusive), and for each `i` in this range, it calculates `i * xs[i]`. This gives the coefficients of the derivative polynomial.

For example, if the input is `[3, 1, 2, 4, 5]`, the function will return `[1, 4, 12, 20]`, which are the coefficients of the derivative polynomial `x + 4x + 12x^2 + 20x^3`. If the input is `[1, 2, 3]`, the function will return `[2, 6]`, which are the coefficients of the derivative polynomial `2 + 6x`. If the input is an empty list, the function will return an empty list.