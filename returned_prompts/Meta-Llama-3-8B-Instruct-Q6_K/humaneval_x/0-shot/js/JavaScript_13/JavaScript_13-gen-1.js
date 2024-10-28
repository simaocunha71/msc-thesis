Here is the solution:

```python
def greatestCommonDivisor(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
```


To explain, the function uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers, `a` and `b`. The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is 0. At that point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure that the result is always positive, even if the input numbers are negative.

Here's an example of how this function could be used:

```python
print(greatestCommonDivisor(3, 5))  # Output: 1
print(greatestCommonDivisor(25, 15))  # Output: 5
```


I hope this helps! Let me know if you have any questions.