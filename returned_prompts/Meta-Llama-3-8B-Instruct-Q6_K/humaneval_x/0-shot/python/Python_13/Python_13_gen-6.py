Here is a Python solution using the Euclidean algorithm:

```python
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```

This function takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The GCD is the largest positive integer that divides both `a` and `b` without leaving a remainder.

The function uses the Euclidean algorithm, which is an efficient method for computing the GCD of two integers. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`.

The `abs` function is used to ensure that the GCD is always positive, even if the input numbers have different signs.

You can test this function with the examples you provided:

```python
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```





