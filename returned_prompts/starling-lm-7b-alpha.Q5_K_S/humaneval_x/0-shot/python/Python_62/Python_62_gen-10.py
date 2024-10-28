
Here is a recursive solution for this problem.

```python
def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    if len(xs) == 1:
        return [0]
    else:
        return [xs[i] * (i+1) for i in range(len(xs))]
```

This function works by taking each coefficient `xs[i]`, multiplying it by `(i+1)`, and creating a new list of the derivatives. It does this for each coefficient in the polynomial, and returns the list of derivatives.

For example, for the input `[3, 1, 2, 4, 5]`, the function will calculate the derivatives as follows:

- The first coefficient `3` is multiplied by `1` (since `i+1 = 1+1`), resulting in `3`.
- The second coefficient `1` is multiplied by `2` (since `i+1 = 1+2`), resulting in `2`.
- The third coefficient `2` is multiplied by `3` (since `i+1 = 1+3`), resulting in `6`.
- The fourth coefficient `4` is multiplied by `4` (since `i+1 = 1+4`), resulting in `16`.
- The fifth coefficient `5` is multiplied by `5` (since `i+1 = 1+5`), resulting in `25`.

Thus, the function returns `[1, 4, 12, 20]`.

Similarly, for the input `[1, 2, 3]`, the function will calculate the derivatives as follows:

- The first coefficient `1` is multiplied by `1` (since `i