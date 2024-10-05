
In this problem we have to find the derivative of a polynomial. The derivative of a polynomial is found by multiplying each term of the polynomial by its corresponding power of x and then subtracting 1 from each power of x. Here's a step-by-step guide on how to solve this problem:

1. Initialize an empty list called `der` that will store the result.
2. Iterate through the list `xs` from left to right. For each element `x` in `xs`, add to `der` the product of `x` and `x-1` raised to the power of the index of `x` in `xs`.
3. Return the result `der`.

The `der` list will contain the derivatives of the polynomial represented by the `xs` list.

Here's the Python code that implements this algorithm:

```python
def derivative(xs: list):
    der = []
    for i, x in enumerate(xs):
        der.append(x * (i + 1))
    return der
```

You can test the function with the following unit tests:

```python
from nose.tools import assert_equal

def test_derivative():
    assert_equal(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
    assert_equal(derivative([1, 2, 3]), [2, 6])

test_derivative()
```

These tests will pass if the `derivative` function is correctly implemented.



















































































































































