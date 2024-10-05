```
const isPrime = (n) => {
  if (n <= 1) {
    return false;
  }
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
};
```


Explanation:

The `isPrime` function takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not.

Here's how it works:

1. If `n` is less than or equal to 1, it's not prime, so we return `false`.
2. We start a loop from 2 and go up to the square root of `n` (inclusive). This is because a larger factor of `n` would be a multiple of a smaller factor that has already been checked.
3. Inside the loop, we check if `n` is divisible by `i` by using the modulo operator (`n % i === 0`). If `n` is divisible, it means `n` has a factor other than 1 and itself, so it's not prime, and we return `false`.
4. If the loop completes without finding a divisor, we return `true`, indicating that `n` is prime.

Note that this function has a time complexity of O(√n), which is efficient for large values of `n`. However, for very large values of `n`, a more advanced algorithm like the Miller-Rabin primality test may be necessary.