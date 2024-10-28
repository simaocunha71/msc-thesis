Here is the solution using a helper function to check if a number is prime:
```javascript
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const xOrY = (n, x, y) => {
  if (isPrime(n)) return x;
  return y;
};
```
Explanation:
The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, it returns `false`, otherwise it returns `true`.

The `xOrY` function simply checks if the input `n` is a prime number using the `isPrime` function. If it is, it returns the value of `x`, otherwise it returns the value of `y`.