```
def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [i * xs[i+1] for i in range(len(xs) - 1)]
```


The derivative of a polynomial is obtained by multiplying each coefficient with its corresponding power and decreasing the power by 1. For example, the derivative of `x^2 + 2x + 3` is `2x + 2`. This is implemented in the code above, where the derivative of a polynomial represented as a list `xs` is computed by multiplying each coefficient with its corresponding power and decreasing the power by 1. The result is also represented as a list.