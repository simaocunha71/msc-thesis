```
def prime_fib(n: int):
    a, b = 1, 1
    count = 1
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


The function `prime_fib(n)` generates Fibonacci numbers and checks if they are prime using the helper function `is_prime(num)`. It keeps generating Fibonacci numbers until it finds the `n`-th prime number. The `is_prime(num)` function checks if a number is prime by checking divisibility up to the square root of the number. The time complexity of this solution is O(n*sqrt(n)) as we need to generate Fibonacci numbers up to the `n`-th prime number and check each number for primality. The space complexity is O(1) as we only need a constant amount of space to store the Fibonacci numbers and the count.