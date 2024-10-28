```javascript
function largestPrimeFactor(n) {
    let maxFactor = 1;
    for (let i = 2; i * i <= n; i++) {
        while (n % i === 0) {
            maxFactor = i;
            n /= i;
        }
    }
    if (n > 1) {
        maxFactor = n;
    }
    return maxFactor;
}
```
This function works by dividing `n` by the smallest prime number (2) as long as it's divisible, then increments to the next smallest prime number (3) and repeats the process until `n` is no longer divisible. The largest prime factor is the last number that `n` was divisible by. If `n` is still greater than 1 after this process, it means that `n` is a prime number itself, so it's returned as the largest prime factor.

For example, for `n = 13195`, the function will divide `n` by 2, then by 3, then by 5, then by 7, then by 11, and finally by 29, which is the largest prime factor. For `n = 2048`, the function will divide `n` by 2, then by 2, then by 2, and finally return 2 as the largest prime factor.