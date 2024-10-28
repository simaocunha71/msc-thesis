```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```


Explanation:
This function calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm. The GCD is the largest positive integer that divides both numbers without a remainder.

The function takes two integers `a` and `b` as input and returns their GCD.

The algorithm works by repeatedly replacing `a` and `b` with `b` and the remainder of `a` divided by `b`, respectively, until `b` becomes zero. At that point, `a` is the GCD of the original `a` and `b`.

The `abs` function is used to return the absolute value of the GCD, because the GCD can be negative if the input numbers have different signs.

The provided unit tests demonstrate the function's correctness for the inputs `3` and `5`, and `25` and `15`. The output for these inputs is `1` and `5`, respectively, which are the correct GCDs.