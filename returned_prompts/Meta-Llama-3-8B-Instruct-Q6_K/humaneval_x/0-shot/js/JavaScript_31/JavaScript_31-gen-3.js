```javascript
const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```
This function checks if a given number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible, it returns `false`, otherwise it returns `true`. The function also returns `false` for numbers less than or equal to 1, as they are not considered prime.