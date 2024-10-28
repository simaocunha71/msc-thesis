Here is a Python solution:
```
def primeFib(n):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
Here's a brief explanation:

The `primeFib` function generates Fibonacci numbers `a` and `b` and checks if `b` is prime using the `is_prime` function. If `b` is prime, it increments a counter `count`. Once `count` reaches `n`, it returns the current value of `b`.

The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the iterated values. If it is, it returns `False`. Otherwise, it returns `True`. Note that we only need to check up to the square root of the number because a larger factor of the number would be a multiple of a smaller factor that has already been checked.

You can test the `primeFib` function with different values of `n` to see the expected results. For example, `primeFib(1)` returns `2`, `primeFib(2)` returns `3`, and so on.