```
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```



The function `is_prime(n)` checks whether a given number `n` is prime or not. It returns `True` if `n` is prime, and `False` otherwise.

The function first checks if `n` is less than 2. If it is, the function returns `False`, because prime numbers are greater than 1.

Then, the function uses a for loop to check if `n` has any divisors other than 1 and itself. It starts the loop from 2 and goes up to the square root of `n` (inclusive). If `n` is divisible by any number in this range, the function returns `False`, because `n` is not prime.

If the loop completes without finding any divisors, the function returns `True`, because `n` is prime.

The unit tests provided in the problem ensure that the function works correctly for a variety of inputs, including prime numbers and non-prime numbers. For example, the test `>>> is_prime(6)` returns `False`, because 6 is not prime. The test `>>> is_prime(101)` returns `True`, because 101 is prime. Similarly, the test `>>> is_prime(11)` returns `True`, because 11 is prime. The test `>>> is_prime(13441)` returns `True`, because 13441 is prime. The test `>>> is_prime(61)` returns `True`, because 61 is prime. The test `>>> is_prime(4)` returns `False`, because 4 is not prime. The test `>>> is_prime(1)` returns `False`, because 1 is not prime.