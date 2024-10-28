```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```
Explanation:
The `isPrime` function takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

Here's a step-by-step breakdown of the function:

1. `if (n <= 1) return false;`: If `n` is less than or equal to 1, it's not prime, so we return `false`.
2. `for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {`: We start a loop from 2 (the smallest prime number) to the square root of `n`. We use the `Math.sqrt` function to calculate the square root of `n` and store it in the `sqrt` variable.
3. `if (n % i === 0) return false;`: Inside the loop, we check if `n` is divisible by `i` using the modulo operator (`%`). If it is, `n` is not prime, so we return `false`.
4. `return true;`: If the loop completes without finding a divisor, `n` is prime, so we return `true`.

Note that we only need to check up to the square root of `n` because a larger factor of `n` would be a multiple of a smaller factor that has already been checked. This optimization helps reduce the number of iterations and improves the function's performance.