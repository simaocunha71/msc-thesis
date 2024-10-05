The problem asks to write a function that takes an integer `n` as input and returns its largest prime factor. The problem assumes that `n` is greater than 1 and is not a prime number.

Here is a Python solution for the problem:

```Python
def largest_prime_factor(n: int):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

The function works by dividing `n` by the smallest prime number, which is 2, as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which is the largest prime factor of `n`.

For example, if `n` is 13195, the function will return 29, which is the largest prime factor of 13195. If `n` is 2048, the function will return 2, which is the largest prime factor of 2048.