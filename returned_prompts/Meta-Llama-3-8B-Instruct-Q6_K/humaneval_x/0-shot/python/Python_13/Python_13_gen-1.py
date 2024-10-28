Here is a Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm:
```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```
Here's an explanation of the code:

1. The function takes two integers `a` and `b` as input.
2. The `while` loop continues until `b` becomes zero.
3. In each iteration, we swap `a` and `b`, and then calculate the remainder of `a` divided by `b` using the modulo operator `%`. This is the key step in the Euclidean algorithm.
4. When `b` becomes zero, `a` is the GCD of the original `a` and `b`.
5. We return the absolute value of `a` to ensure that the result is positive.

The function is tested with the examples provided in the question:
```
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
Note that this implementation assumes that the input integers are non-negative. If you need to handle negative integers, you can add a simple check at the beginning of the function to make `a` and `b` positive. For example:
```
def greatest_common_divisor(a: int, b: int) -> int:
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a
``` A: Here is a Python function that calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm:
```
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
```
Here's an explanation of the code:

1. The function takes two integers `a` and `b` as input.
2. The `while` loop continues until `b` becomes zero.
3. In each iteration, we swap `a` and `b`, and then calculate the remainder of `a` divided by `b` using the modulo operator `%`. This is the key step in the Euclidean algorithm.
4. When `b` becomes zero, `a` is the