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
        if len(primes) == n:
            break
    return primes
```


This function uses a helper function `is_prime` to check if a number is prime. It then iterates over the numbers from 2 to `n-1` and adds the prime numbers to the `primes` list. Once it has found `n` prime numbers, it returns the list. If `n` is 0 or 1, the function returns an empty list because there are no prime numbers less than 0 or 1.