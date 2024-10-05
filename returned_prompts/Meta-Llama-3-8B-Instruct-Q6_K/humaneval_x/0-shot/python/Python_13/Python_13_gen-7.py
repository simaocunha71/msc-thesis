```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```


This function uses the Euclidean algorithm to find the greatest common divisor (GCD) of two integers `a` and `b`. The GCD is the largest positive integer that divides both `a` and `b` without leaving a remainder.

The function works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` is zero. At that point, `a` is the GCD of the original `a` and `b`.

The `abs` function is used to ensure that the GCD is positive, even if the original `a` and `b` were negative.

The time complexity of this function is O(log min(a, b)), where `min(a, b)` is the smaller of the two input integers. This is because the function reduces the problem size by at least half in each iteration, until the problem size is reduced to zero. The space complexity is O(1), because the function only uses a constant amount of space to store the temporary values of `a` and `b`.