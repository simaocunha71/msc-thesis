```python
def greatestCommonDivisor(a, b):
    while b:
        a, b = b, a % b
    return abs(a)
```
Explanation:
The function uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers `a` and `b`. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` becomes zero. At that point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to return the absolute value of the GCD, since the GCD is always non-negative.

This function works for both positive and negative integers, and it also works for zero, returning the GCD as 0. For example, `greatestCommonDivisor(3, 5)` returns 1, and `greatestCommonDivisor(25, 15)` returns 5.