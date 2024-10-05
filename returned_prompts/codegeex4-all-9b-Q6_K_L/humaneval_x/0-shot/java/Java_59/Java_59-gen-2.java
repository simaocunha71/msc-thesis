Here is a simple solution in Java:

```java
public int largestPrimeFactor(int n) {
    int i;
    for(i = 2; i <= n; i++) {
        if(n % i == 0) {
            n = n / i;
            i--;
        }
    }
    return i;
}
```

This solution works by dividing `n` by `i` while `i` is less than or equal to `n`. If `n` is divisible by `i`, then `i` is a factor of `n` and we divide `n` by `i` to get a new `n`. We then decrement `i` by 1 to check for any other factors of the new `n`. This process repeats until `i` is greater than `n`.

Finally, `i` is the largest prime factor of the original `n`. We return `i` as the result.

Note that this solution is not the most efficient for large numbers. For a more efficient solution, you can use the Sieve of Eratosthenes algorithm to find all prime numbers up to `n`, and then check which of these primes divide `n` without a remainder.