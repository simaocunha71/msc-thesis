```
def prime_fib(n: int):
    if n <= 0:
        raise ValueError("n must be a positive integer")

    a, b = 0, 1
    count = 0

    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b


def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```



Explanation:

1. The function `prime_fib` takes an integer `n` as input and returns the `n-th` number that is both a Fibonacci number and a prime number.
2. The function first checks if `n` is less than or equal to 0, and if so, raises a `ValueError` because `n` must be a positive integer.
3. The function then initializes two variables `a` and `b` to 0 and 1, respectively, which are the first two Fibonacci numbers.
4. The function then enters a loop that continues indefinitely until the desired Fibonacci number is found.
5. Inside the loop, the function calculates the next Fibonacci number by assigning `b` to `a` and `a + b` to `b`.
6. The function then checks if the new Fibonacci number `b` is prime using the `is_prime` function.
7. If `b` is prime, the function increments a counter `count` to keep track of the number of prime Fibonacci numbers found.
8. If `count` equals `n`, the function returns the `n-th` prime Fibonacci number.
9. The `is_prime` function takes an integer `num` as input and returns `True` if it is prime, and `False` otherwise.
10. The `is_prime` function first checks if `num` is less than 2, in which case it is not prime.
11. The function then checks if `num` is divisible by any integer `i` from 2 to the square root of `num` (inclusive). If it is, then `num` is not prime.
12. If `num` is not divisible by any `i` in the range, then it is prime, and the function returns `True`.

Note that the `