```
def is_not_prime(n):
    if n <= 1:
        return True
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False
```
This function checks if a given number is not prime. It first handles the special cases of 0, 1, and the first few prime numbers. Then it checks if the number is divisible by any number up to its square root. If it is, then the number is not prime. If not, then it is prime. The function returns True if the number is not prime and False if it is. 

The unit test `assert is_not_prime(2) == False` ensures that the function correctly identifies prime numbers. It should return False for prime numbers and True for non-prime numbers. 

Please note that this function is not optimized for large numbers as it checks divisibility up to the square root of the number. For large numbers, a more efficient algorithm such as the Miller-Rabin primality test may be needed. 