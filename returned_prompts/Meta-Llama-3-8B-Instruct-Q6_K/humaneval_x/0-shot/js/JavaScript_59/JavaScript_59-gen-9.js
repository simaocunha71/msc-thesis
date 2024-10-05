Here is a Python solution that calculates the largest prime factor of a given number `n`:

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

This function works by dividing `n` by the smallest prime number (2) as long as it's divisible. Then it increments the divisor until it finds the next number that can divide `n`, which will be a prime number. This process continues until `n` is reduced to its largest prime factor. The remaining `n` value is the largest prime factor.

For example, if you call `largestPrimeFactor(13195)`, it will return `29`, and if you call `largestPrimeFactor(2048)`, it will return `2`. 

The time complexity of this algorithm is O(sqrt(n)) because it iterates up to the square root of `n`. The space complexity is O(1) because it only uses a constant amount of space to store the variables. 

This solution assumes that `n` is greater than 1 and is not a prime number, as specified in the problem statement. If `n` is prime, the function will return `n` itself. If `n` is less than or equal to 1, the function will not work correctly. 

In the provided unit tests, the input `13195` has a largest prime factor of `29`, and the input `2048` has a largest prime factor of `2`. The function correctly returns these values. 