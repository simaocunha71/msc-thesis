Here is the solution to the problem:
```
const largestPrimeFactor = (n) => {
  let maxFactor = 1;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      let factor = i;
      while (n % factor === 0) {
        maxFactor = factor;
        n /= factor;
      }
    }
  }
  if (n > 1) {
    maxFactor = n;
  }
  return maxFactor;
};
```
Here's an explanation of the code:

1. We start by initializing `maxFactor` to 1, which will store the largest prime factor of `n`.
2. We loop from 2 to the square root of `n` (inclusive). This is because a larger factor of `n` must be a multiple of a smaller factor that has already been checked.
3. For each `i` in the loop, we check if `n` is divisible by `i` using the modulo operator (`n % i === 0`). If it is, we have found a factor of `n`.
4. We then loop until `n` is no longer divisible by `i`, updating `maxFactor` to the largest factor found. We divide `n` by `i` at each iteration to reduce the value of `n`.
5. If `n` is still greater than 1 after the loop, it means that `n` itself is a prime number, so we update `maxFactor` to `n`.
6. Finally, we return `maxFactor`, which is the largest prime factor of `n`.

Note that this algorithm has a time complexity of O(√n), which is efficient for large values of `n`. However, for very large values of `n`, a more advanced algorithm may be needed.