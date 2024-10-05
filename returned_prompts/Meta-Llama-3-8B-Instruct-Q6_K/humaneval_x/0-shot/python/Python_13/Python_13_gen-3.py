```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```
The function takes two integers as input and returns their greatest common divisor (GCD). It uses the Euclidean algorithm to find the GCD. The function works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, until `b` becomes 0. At that point, `a` is the GCD of the original `a` and `b`.

The function uses the `while` loop to repeatedly apply the Euclidean algorithm until `b` becomes 0. In each iteration, it updates `a` and `b` to be `b` and the remainder of `a` divided by `b`, respectively. When `b` becomes 0, the function returns the absolute value of `a`, which is the GCD of the original `a` and `b`.

The unit tests provided in the problem statement demonstrate the function's correctness. For example, `greatest_common_divisor(3, 5)` returns 1, which is the GCD of 3 and 5. Similarly, `greatest_common_divisor(25, 15)` returns 5, which is the GCD of 25 and 15.