The function `largest_prime_factor` takes an integer `n` as input and returns the largest prime factor of `n`.

Here is the solution:
```python
def largest_prime_factor(n: int):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```
Explanation:

1. We start with `i = 2`, which is the smallest prime number.
2. We loop until `i * i` is greater than `n`. This is because if `n` has a factor greater than `i`, it must have a factor less than or equal to `i`.
3. Inside the loop, we check if `n` is divisible by `i`. If it is, we divide `n` by `i` and continue the loop.
4. If `n` is not divisible by `i`, we increment `i` by 1 and continue the loop.
5. Once the loop finishes, `n` is the largest prime factor of the original `n`.

For example, if `n = 13195`, the function will return `29`, which is the largest prime factor of `13195`. If `n = 2048`, the function will return `2`, which is the largest prime factor of `2048`.

Note: This function assumes that `n` is greater than 1 and is not a prime number. If `n` is a prime number, the function will return `n` itself. If `n` is less than or equal to 1, the function will return an error.