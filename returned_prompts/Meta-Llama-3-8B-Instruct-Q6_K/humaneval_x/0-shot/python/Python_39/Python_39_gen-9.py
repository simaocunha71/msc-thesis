```
def prime_fib(n: int):
    a, b = 0, 1
    i = 1
    while True:
        a, b = b, a + b
        if b >= n:
            break
        if is_prime(b):
            i += 1
            if i == n:
                return b

def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
This solution generates Fibonacci numbers and checks if they are prime using the `is_prime` function. It stops when it finds the nth Fibonacci number that is prime. The `is_prime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it's not divisible, the number is prime.

The time complexity of this solution is O(n*sqrt(n)) because it generates Fibonacci numbers up to the nth number and checks if each number is prime. The space complexity is O(1) because it only uses a constant amount of space to store the Fibonacci numbers and the prime number.