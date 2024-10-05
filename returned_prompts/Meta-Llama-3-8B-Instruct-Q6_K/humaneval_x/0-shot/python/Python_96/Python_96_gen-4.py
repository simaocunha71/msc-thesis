```
def count_up_to(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
        if len(primes) == n - 1:
            break
    return primes
```
This function uses a helper function `is_prime` to check if a number is prime. It then iterates over the numbers from 2 to `n-1` and adds the prime numbers to a list. It stops when it has found `n-1` prime numbers. The function returns this list of prime numbers.

For example, if you call `count_up_to(5)`, the function will return `[2, 3]`, which are the first two prime numbers less than 5. If you call `count_up_to(11)`, the function will return `[2, 3, 5, 7]`, which are the first four prime numbers less than 11. If you call `count_up_to(0)`, the function will return an empty list, because there are no prime numbers less than 0. If you call `count_up_to(1)`, the function will also return an empty list, because there are no prime numbers less than 1. If you call `count_up_to(20)`, the function will return `[2, 3, 5, 7, 11, 13, 17, 19]`, which are the first eight prime numbers less than 20. And so on.