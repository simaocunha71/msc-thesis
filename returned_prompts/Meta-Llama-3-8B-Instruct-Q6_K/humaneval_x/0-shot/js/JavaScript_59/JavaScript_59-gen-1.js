```javascript
function largestPrimeFactor(n) {
  let maxFactor = 1;
  for (let i = 2; i * i <= n; i++) {
    while (n % i === 0) {
      maxFactor = i;
      n /= i;
    }
  }
  return maxFactor;
}
```


Explanation:
The function `largestPrimeFactor` takes an integer `n` as input and returns the largest prime factor of `n`. We start by initializing `maxFactor` to 1, which will be updated to the largest prime factor found.

We then loop through all numbers from 2 to the square root of `n` (inclusive). For each number `i` in this range, we check if `n` is divisible by `i` by using the modulo operator (`n % i === 0`). If `n` is divisible by `i`, we update `maxFactor` to `i` and divide `n` by `i`. This process is repeated until `n` is no longer divisible by `i`.

Once the loop completes, `maxFactor` will hold the largest prime factor of `n`. We return `maxFactor` as the result.

For example, if we call `largestPrimeFactor(13195)`, the function will iterate through numbers from 2 to 121 (the square root of 13195), and find that 29 is the largest prime factor, so it returns 29. If we call `largestPrimeFactor(2048)`, the function will find that 2 is the largest prime factor, so it returns 2.