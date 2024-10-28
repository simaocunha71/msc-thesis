```
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def newman_prime(n):
    i = 1
    count = 0
    while True:
        i += 1
        if is_prime(i):
            count += 1
        if count == n:
            return i
```    
The `newman_prime` function finds the nth Newman-Shanks-Williams prime number. It uses a helper function `is_prime` to check if a number is prime. It starts from 1 and increments by 1 in each iteration, and checks if the current number is prime using `is_prime`. If it is, it increments a counter. When the counter reaches `n`, it returns the current number as the nth Newman-Shanks-Williams prime number.

The `is_prime` function checks if a number is prime by testing divisibility up to the square root of the number. If the number is divisible by any of the numbers in the range, it is not prime. Otherwise, it is prime. This function is used by `newman_prime` to check if a number is prime.