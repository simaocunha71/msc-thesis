Here is a Python solution for the problem:

```Python
def largestPrimeFactor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largestPrimeFactor(13195))  # Output: 29
print(largestPrimeFactor(2048))   # Output: 2
```

The function `largestPrimeFactor` takes an integer `n` as input and returns the largest prime factor of `n`. The function works by dividing `n` by the smallest prime number (2) as long as `n` is divisible by 2. This is done by the while loop. If `n` is not divisible by 2, it means that the smallest prime factor of `n` is greater than 2, so the function increments `i` by 1. This process continues until `i` is greater than the square root of `n`. At this point, `n` is a prime number or the largest prime factor of the original `n`. Therefore, the function returns `n`. If `n` is a prime number, the function returns `n` itself. This is because the largest prime factor of a prime number is the prime number itself. 

The time complexity of this function is O(sqrt(n)) because it needs to iterate up to the square root of `n` to find the largest prime factor. The space complexity is O(1) because it only uses a constant amount of space to store the variables `i` and `n`. 