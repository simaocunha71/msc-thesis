The problem is asking to find the largest prime factor of a given number n. 

Here is a Python solution:

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

This function works by dividing the number n by the smallest prime number (2) as long as it is divisible. Then it increments the divisor until it finds the next number that can divide n, which will be a prime number. This process continues until n is reduced to its largest prime factor.

For example, if we call `largest_prime_factor(13195)`, the function will return `29`, which is the largest prime factor of `13195`. Similarly, `largest_prime_factor(2048)` will return `2`, which is the largest prime factor of `2048`. 

This function assumes that the input number `n` is greater than 1 and is not a prime number, as stated in the problem. If `n` is a prime number, the function will return `n` itself. If `n` is less than or equal to 1, the function will return an incorrect result. 

Note that this function is not efficient for large numbers, as it has a time complexity of O(sqrt(n)). For large numbers, a more efficient algorithm is needed. 