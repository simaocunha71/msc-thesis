```
def count_Primes_nums(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    p = 2
    while p * p < n:
        if primes[p]:
            for i in range(p * p, n, p):
                primes[i] = False
        p += 1
    return sum(1 for p in primes if p)
```    
    This function uses the Sieve of Eratosthenes algorithm to find all prime numbers less than the given number. It starts by assuming all numbers are prime, then iteratively marks the multiples of each prime number starting from 2. The function then counts the number of prime numbers found. The unit test `assert count_Primes_nums(5) == 2` ensures the function correctly returns the number of prime numbers less than 5, which is 2 (2 and 3).   


The function starts by initializing a list `primes` of boolean values, where `primes[i]` is `True` if `i` is prime and `False` otherwise. It then sets `primes[0]` and `primes[1]` to `False`, since 0 and 1 are not prime.

The function then iterates over the numbers from 2 to the square root of `n`. For each prime `p` in this range, it sets `primes[i]` to `False` for all multiples `i` of `p`, starting from `p * p`. This is because all multiples of `p` greater than `p` must be composite (i.e., not prime).

Finally, the function returns the sum of the boolean values in the `primes` list, which represents the number of prime numbers less than `n`.   


The time complexity of this function is O(n log log n) and the space complexity is O(n).   


The unit test `assert count_Primes_nums(5) == 2` ensures that the function correctly returns the number of prime numbers less than 5, which is 2 (2 and 3).   


The function can be further optimized by only iterating up to the square root of `n` when checking for multiples of each prime number. This is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.   


The function can