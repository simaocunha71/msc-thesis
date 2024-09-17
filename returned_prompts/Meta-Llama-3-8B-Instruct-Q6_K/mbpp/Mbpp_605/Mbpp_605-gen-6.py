```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```
The function `prime_num(n)` checks if the given integer `n` is a prime number. It does this by checking if `n` is divisible by any integer from 2 to `n-1`. If `n` is divisible by any of these integers, then it is not a prime number and the function returns `False`. If `n` is not divisible by any of these integers, then it is a prime number and the function returns `True`. 

The unit test `assert prime_num(13)==True` ensures that the function correctly identifies 13 as a prime number. 

Note: This function is not efficient for large numbers because it checks divisibility for all integers from 2 to `n-1`. For a more efficient solution, you can use the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to a certain limit, and then check if the given number is in this list.  Alternatively, you can use a more advanced primality test such as the Miller-Rabin primality test.  However, for small numbers, the simple function above should be sufficient. 