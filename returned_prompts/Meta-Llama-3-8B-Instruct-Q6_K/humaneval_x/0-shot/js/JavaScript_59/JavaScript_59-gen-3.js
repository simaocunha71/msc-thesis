Here is a Python solution for the problem:

```
def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

Explanation:
The function `largestPrimeFactor` takes an integer `n` as input and returns the largest prime factor of `n`. The function works by dividing `n` by the smallest prime number `i` (which starts at 2) as long as `n` is divisible by `i`. This process is repeated until `i * i` is greater than `n`. At this point, `n` is the largest prime factor of the original number. The function returns `n`.

For example, when `n` is 13195, the function will divide 13195 by 2, 3, 5, and 7, and return 29, which is the largest prime factor. When `n` is 2048, the function will return 2, which is the largest prime factor.