```python
def count_Primes_nums(n):
    if n <= 2:
        return 0
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = [False] * ((n - i * i - 1) // (i - 1) + 1)
    return sum(sieve)
```
