```javascript
const xOrY = (n, x, y) => {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
Explanation:
This program defines two functions, `xOrY` and `isPrime`. The `xOrY` function takes three arguments: `n`, `x`, and `y`. It checks if `n` is a prime number using the `isPrime` function. If `n` is prime, it returns `x`; otherwise, it returns `y`.

The `isPrime` function checks if a given number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it returns `false`; otherwise, it returns `true`.

For example, `xOrY(7, 34, 12)` would return `34` because 7 is a prime number, and `xOrY(15, 8, 5)` would return `5` because 15 is not a prime number.