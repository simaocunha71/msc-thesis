```
def largest_prime_factor(n: int):
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_prime = i
    return largest_prime
```


The function `largest_prime_factor` calculates the largest prime factor of a given number `n`. The helper function `is_prime` checks whether a number is prime or not.

The function starts by checking if the number `n` is divisible by any number from 2 to `n` and if that number is prime. If it is, then it updates the `largest_prime` variable with the new prime factor.

Finally, the function returns the `largest_prime` variable which holds the largest prime factor of the given number `n`.

The function is tested with the examples provided in the problem statement. The first example is `largest_prime_factor(13195)` which returns `29` and the second example is `largest_prime_factor(2048)` which returns `2`.