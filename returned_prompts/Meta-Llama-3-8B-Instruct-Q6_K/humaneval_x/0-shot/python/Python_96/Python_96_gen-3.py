```
def count_up_to(n):
    if n < 1:
        return []
    primes = []
    num = 2
    while num < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```
The function `count_up_to(n)` takes an integer `n` and returns a list of all prime numbers less than `n`. It uses a helper function `is_prime(num)` to check whether a number is prime or not.

The `is_prime(num)` function takes an integer `num` and returns `True` if it is prime, and `False` otherwise. It does this by checking if `num` is less than 2, in which case it is not prime, or if `num` is divisible by any number from 2 to the square root of `num`, in which case it is not prime. If `num` passes these checks, it is prime.

The `count_up_to(n)` function uses a while loop to iterate over all numbers from 2 to `n-1`, and for each number, it checks if it is prime using the `is_prime(num)` function. If it is prime, it adds it to the list of primes. Finally, it returns the list of primes.

Note that the `is_prime(num)` function has a time complexity of O(sqrt(n)), and the `count_up_to(n)` function has a time complexity of O(n*sqrt(n)), which can be slow for large values of `n`. There are more efficient algorithms for finding prime numbers, such as the Sieve of Eratosthenes, but they are also more complex.