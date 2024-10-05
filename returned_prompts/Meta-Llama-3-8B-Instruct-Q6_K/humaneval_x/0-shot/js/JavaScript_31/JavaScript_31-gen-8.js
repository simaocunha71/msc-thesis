```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```


Explanation:
The function `isPrime` takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number or not.

The function first checks if `n` is less than or equal to 1, in which case it returns `false`, since 0 and 1 are not prime numbers.

Then, it iterates from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by any of these numbers. If it is, the function returns `false`, since `n` is not prime.

If the function reaches the end of the loop without finding a divisor, it returns `true`, indicating that `n` is a prime number. This is because a prime number has only two distinct factors: 1 and itself. Since the loop only checks up to the square root of `n`, we can be sure that if `n` has a divisor greater than its square root, it would have been found earlier in the loop.