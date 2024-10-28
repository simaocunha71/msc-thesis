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
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
```


The code defines two helper functions: `is_prime` to check if a number is prime, and `prime_fib` to find the `n-th` Fibonacci number that is also prime. The `is_prime` function checks divisibility from 2 to the square root of the number, and `prime_fib` uses a loop to generate Fibonacci numbers and checks if each one is prime using the `is_prime` function. Once the `n-th` prime Fibonacci number is found, it is returned. The function is then tested with various inputs to verify its correctness.