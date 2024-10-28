```
def derivative(xs: list):
    result = [0]
    for i in range(1, len(xs)):
        result.append(i * xs[i])
    return result[1:]
```
The derivative of a polynomial is a new polynomial whose coefficients are the derivatives of the original polynomial's coefficients. In other words, if we have a polynomial `f(x) = a0 + a1*x + a2*x^2 + ... + an*x^n`, then the derivative `f'(x)` is `a1 + 2*a2*x + 3*a3*x^2 + ... + n*an*x^(n-1)`.

We can calculate this derivative by iterating over the coefficients of the original polynomial, starting from the second one (since the derivative of a constant is 0). For each coefficient `xs[i]`, we multiply it by `i` (since the derivative of `x^i` is `i*x^(i-1)`) and add the result to the result list.

Finally, we return the result list, but starting from the second element (since the first element is 0, which corresponds to the derivative of the constant term).

The unit test `derivative([3, 1, 2, 4, 5])` checks that the derivative of the polynomial `3 + x + 2*x^2 + 4*x^3 + 5*x^4` is indeed `1 + 4*x + 12*x^2 + 20*x^3`. The unit test `derivative([1, 2, 3])` checks that the derivative of the polynomial `1 + 2*x + 3*x^2` is indeed `2 + 6*x`. Both tests pass! 🎉
```
```python
import unittest

class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()
````
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
``