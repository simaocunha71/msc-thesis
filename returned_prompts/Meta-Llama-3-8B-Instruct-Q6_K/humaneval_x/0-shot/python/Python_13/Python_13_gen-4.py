```
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)
```
This code defines a function `greatest_common_divisor` that takes two integers `a` and `b` as input and returns their greatest common divisor (GCD). The function uses the Euclidean algorithm to find the GCD.

Here's a breakdown of how the function works:
1. The function takes two integers `a` and `b` as input and initializes the GCD to `a`.
2. The function enters a loop that continues until `b` is zero.
3. In each iteration, the function updates `a` to be the value of `b` and updates `b` to be the remainder of `a` divided by `b`. This is the key step in the Euclidean algorithm, which reduces the problem of finding the GCD of `a` and `b` to finding the GCD of `b` and the remainder of `a` divided by `b`.
4. Once `b` is zero, the function returns the absolute value of `a`, which is the GCD of the original `a` and `b`.

The function is tested with the following examples:
```
>>> greatest_common_divisor(3, 5)
1
>>> greatest_common_divisor(25, 15)
5
```
These examples demonstrate that the function correctly returns the GCD of the input integers.