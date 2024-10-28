```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```

Explanation:
The function `greatest_common_divisor` calculates the greatest common divisor (GCD) of two integers `a` and `b`. It uses the Euclidean algorithm, which is an efficient method for computing the GCD of two numbers.

The algorithm works by repeatedly replacing `a` with `b` and `b` with the remainder of `a` divided by `b`, until `b` becomes 0. At that point, `a` is the GCD of the original `a` and `b`.

The `while` loop continues until `b` becomes 0. In each iteration, the values of `a` and `b` are updated to be `b` and the remainder of `a` divided by `b`, respectively.

Finally, the function returns the absolute value of `a`, which is the GCD of the original `a` and `b`. The absolute value is taken to handle the case where the GCD is negative, which can occur if the original `a` and `b` have opposite signs.

The function is tested with the examples provided in the problem statement, which demonstrate its correctness. The first example, `greatest_common_divisor(3, 5)`, returns 1, which is the GCD of 3 and 5. The second example, `greatest_common_divisor(25, 15)`, returns 5, which is the GCD of 25 and 15.