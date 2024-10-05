```
def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return abs(a)
```


The `greatest_common_divisor` function takes two integers `a` and `b` as input and returns their greatest common divisor. The function uses the Euclidean algorithm to find the GCD. The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` becomes 0. At that point, `a` is the GCD of the original `a` and `b`. The `abs` function is used to ensure that the GCD is always positive.

The unit tests provided demonstrate that the function works correctly for the given inputs. For example, the test `greatest_common_divisor(3, 5)` returns `1`, which is the GCD of 3 and 5. Similarly, the test `greatest_common_divisor(25, 15)` returns `5`, which is the GCD of 25 and 15.