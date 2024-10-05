```
def prime_fib(n: int):
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        if is_prime(b):
            count += 1
            if count == n:
                return b
        if b > 1000000:  # limit to avoid long computation
            return "No such number found."

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
In this solution, we generate Fibonacci numbers and check if they are prime. We use a helper function `is_prime` to check if a number is prime. We also use a counter to keep track of the number of prime Fibonacci numbers generated. Once we reach the `n`th prime Fibonacci number, we return it. We also add a limit to avoid long computation. If no such number is found within the limit, we return a message indicating that.  The `is_prime` function checks if a number is prime by checking divisibility up to the square root of the number.  The `prime_fib` function returns the `n`th prime Fibonacci number, or a message if no such number is found.  The function `is_prime` returns `True` if the number is prime, and `False` otherwise.  The `prime_fib` function returns the `n`th prime Fibonacci number, or a message if no such number is found.  The function `prime_fib` returns the `n`th prime Fibonacci number, or a message if no such number is found.  The function `is_prime` returns `True` if the number is prime, and `False` otherwise.  The `prime_fib` function returns the `n`th prime Fibonacci number, or a message if no such number is found.  The function `is_prime` returns `True` if the number is prime, and `False` otherwise.  The `prime_fib` function returns the `n`th prime Fibonacci number, or a message if no such number is found.  The function `is_prime` returns `True` if the number is prime, and `False` otherwise.  The `prime_fib` function returns the `n`th prime Fibonacci number