```
def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return True
    return False
```
This function checks if a number is not prime by iterating from 2 to n-1 and checking if n is divisible by any of these numbers. If it is, then n is not a prime number. If it's not divisible by any of these numbers, then n is a prime number. The function returns True if the number is not prime and False if it's prime.

The unit test `assert is_not_prime(2) == False` ensures that the function returns False for prime numbers. In this case, the function should return False because 2 is a prime number.