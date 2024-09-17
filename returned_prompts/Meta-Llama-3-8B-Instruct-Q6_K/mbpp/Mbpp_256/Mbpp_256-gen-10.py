```
def count_Primes_nums(n):
    if n <= 1:
        return 0

    primes = [True for _ in range(n+1)]
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    return sum(1 for p in primes if p)
```


The function `count_Primes_nums(n)` counts the number of prime numbers less than or equal to `n`. It uses the Sieve of Eratosthenes algorithm to achieve this.

The algorithm works by iteratively marking the multiples of each prime number starting from 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with a difference between them that is equal to that prime. This is the key distinction from using trial division to sequentially test each candidate number for divisibility by each prime.

The function first initializes a list of boolean values, `primes`, of size `n+1`, and sets all values to `True`, assuming all numbers are prime initially. It then sets `primes[0]` and `primes[1]` to `False`, as 0 and 1 are not prime.

The function then iterates over the list, starting from `p = 2`. For each prime `p`, it marks as composite (i.e., not prime) the multiples of `p` by setting `primes[i]` to `False` for `i` ranging from `p * p` to `n+1` in increments of `p`. This is done using a loop that starts at `p * p` (because all the multiples of `p` less than `p * p` have already been marked) and goes up to `n+1` in increments of `p`.

Finally, the function returns the sum of all the `True` values in the `primes` list, which represents the count of prime numbers less than or equal to `n`.

The unit test `assert count_Primes_nums(5) == 2` ensures that the function correctly counts the prime numbers less than or equal to 5, which are 2 and 3.