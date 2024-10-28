```
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    a, b = 0, 1
    count = 0
    while count < n:
        a, b = b, a + b
        if is_prime(b):
            count += 1
    return b
```


The `is_prime` function checks if a number is prime. It does this by checking if the number is divisible by any number up to its square root. If it is divisible, it's not a prime number.

The `prime_fib` function generates Fibonacci numbers and checks if they are prime. It does this by maintaining two variables `a` and `b` that hold the previous two Fibonacci numbers. It increments the count whenever it finds a prime Fibonacci number. Finally, it returns the `n`-th prime Fibonacci number.

Note that the `is_prime` function has a time complexity of O(sqrt(n)), and the `prime_fib` function has a time complexity of O(n*sqrt(n)). Therefore, this solution is not efficient for large values of `n`. There are more efficient algorithms to find prime Fibonacci numbers, but they are more complex to implement.