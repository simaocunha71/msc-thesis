```javascript
const xOrY = (n, x, y) => {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
};

function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(xOrY(7, 34, 12)); // returns 34
console.log(xOrY(15, 8, 5)); // returns 5
```
Explanation:
The function `xOrY` takes three arguments: `n`, `x`, and `y`. It uses the `isPrime` function to check if `n` is a prime number. If `n` is prime, it returns the value of `x`; otherwise, it returns the value of `y`.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns `false`, indicating that the number is not prime. If the number is not divisible by any of these values, the function returns `true`, indicating that the number is prime.

In the examples, `xOrY(7, 34, 12)` returns `34` because 7 is a prime number, and `xOrY(15, 8, 5)` returns `5` because 15 is not a prime number.