
The derivative of a polynomial is a polynomial of the same degree. The degree of the derivative is one more than the degree of the original polynomial.

The derivative of a polynomial with coefficients $a_0, a_1, a_2, \ldots$ is obtained by multiplying each coefficient by the corresponding power of $x$ and then decrementing the exponent by one.

In other words, if $P(x) = a_0 + a_1x + a_2x^2 + \cdots$, then $P'(x) = a_1 + 2a_2x + 3a_3x^2 + \cdots$.

Here is a Python function that computes the derivative of a polynomial from a list of coefficients:

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
    # Create a new list to store the derivative.
    result = [0] * len(xs)
    
    # For each coefficient, compute the corresponding derivative.
    for i in range(len(xs)):
        result[i] = xs[i] * (i + 1)
        
    # Return the derivative as a list.
    return result
```

For example, if $P(x) = 3 + x + 2x^2 + 4x^3 + 5x^4$, then $P'(x) = 1 + 2(2)x + 3(4)x^2 + 4(5)x^3 = 1 + 4x + 12x^2 + 20x^3$.

To compute the derivative, the function multiplies each coefficient by the corresponding power of $x$ and then decrements the exponent by one. The function returns the derivative as a list.

For example, if we call `