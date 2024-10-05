The problem asks you to write a function that returns the largest prime factor of a given number `n`. The function should work for numbers greater than 1 and not prime.

Here is a Python solution for the problem:

```Python
def LargestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

This function works by dividing `n` by the smallest prime number (2) as long as it is divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process continues until `n` is reduced to its largest prime factor.

For example, if you call `LargestPrimeFactor(13195)`, the function will return `29`, which is the largest prime factor of `13195`. Similarly, if you call `LargestPrimeFactor(2048)`, the function will return `2`, which is the largest prime factor of `2048`.