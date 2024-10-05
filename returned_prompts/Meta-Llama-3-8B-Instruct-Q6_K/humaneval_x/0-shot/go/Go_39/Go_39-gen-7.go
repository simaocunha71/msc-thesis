The problem is asking you to write a function that returns the nth Fibonacci number that is also a prime number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

Here is a Python solution for the problem:

```Python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def PrimeFib(n):
    a, b = 0, 1
    count = 0
    for _ in range(n):
        a, b = b, a + b
        if is_prime(b):
            count += 1
        if count == n:
            return b
```

This solution uses a helper function `is_prime` to check if a number is prime. The `PrimeFib` function generates Fibonacci numbers and checks if they are prime. It returns the nth prime Fibonacci number. The function uses a loop to generate Fibonacci numbers and a counter to keep track of the number of prime Fibonacci numbers found. When the counter reaches `n`, the function returns the nth prime Fibonacci number.

Note that this solution is not efficient for large values of `n` because it checks every Fibonacci number to see if it is prime. A more efficient solution would be to use a sieve to generate prime numbers and then check if the Fibonacci numbers are in the sieve. However, this would be a more complex solution and would require additional code.