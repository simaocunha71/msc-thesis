Here is a Python solution for the problem:

```python
def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
```

This function works by dividing `n` by the smallest prime number (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process is repeated until `n` is reduced to its largest prime factor. 

For example, if we call `largestPrimeFactor(13195)`, the function will return `29` because `29` is the largest prime factor of `13195`. If we call `largestPrimeFactor(2048)`, the function will return `2` because `2` is the largest prime factor of `2048`. 

This function is efficient because it only needs to iterate up to the square root of `n` to find its largest prime factor. This is because a larger factor of `n` must be a multiple of a smaller factor that has already been found. 

The time complexity of this function is O(sqrt(n)) and the space complexity is O(1), making it efficient for large inputs. 