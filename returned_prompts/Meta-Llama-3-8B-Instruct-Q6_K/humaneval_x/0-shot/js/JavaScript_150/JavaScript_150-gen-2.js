```javascript
const xOrY = (n, x, y) => {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
};

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i < Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}
```
The `xOrY` function checks if the number `n` is prime using the `isPrime` helper function. If `n` is prime, it returns `x`, otherwise it returns `y`. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the numbers in that range. If it is, it returns `false`, otherwise it returns `true`.