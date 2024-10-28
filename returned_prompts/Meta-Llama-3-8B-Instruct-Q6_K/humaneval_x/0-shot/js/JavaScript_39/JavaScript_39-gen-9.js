Here is a Python solution for this problem. This function generates Fibonacci numbers until it finds the nth prime Fibonacci number.

```Python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def primeFib(n):
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
```

This function works by generating Fibonacci numbers and checking if they are prime. The `is_prime` function checks if a number is prime. The `primeFib` function generates Fibonacci numbers until it finds the nth prime Fibonacci number. It keeps track of the count of prime Fibonacci numbers and returns the nth one.

The function `is_prime` checks if a number is prime by trying to divide it by all numbers up to its square root. If it finds a divisor, it returns `False`. If it doesn't find any divisors, it returns `True`.

The function `primeFib` generates Fibonacci numbers using a loop. It keeps track of the last two Fibonacci numbers `a` and `b`. In each iteration, it updates `a` and `b` to be `b` and `a + b` respectively. It then checks if `b` is prime using the `is_prime` function. If it is, it increments the count of prime Fibonacci numbers. If the count is equal to `n`, it returns `b`. Otherwise, it continues generating Fibonacci numbers.

This function is not very efficient for large values of `n` because it generates all Fibonacci numbers until it finds the nth prime one. It would be more efficient to generate only the prime Fibonacci numbers and stop when it finds the nth one. However, this would require a more complex algorithm.