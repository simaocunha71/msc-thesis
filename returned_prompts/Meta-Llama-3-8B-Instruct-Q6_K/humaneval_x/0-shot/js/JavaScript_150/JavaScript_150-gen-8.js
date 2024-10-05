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
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```

Explanation:
The given problem is asking to create a function `xOrY` which takes three parameters `n`, `x` and `y`. This function should return the value of `x` if `n` is a prime number, otherwise it should return the value of `y`.

We can solve this problem by creating another helper function `isPrime` which checks if a number is prime or not. This `isPrime` function checks if the number is less than or equal to 1, if it is, then it's not a prime number. Then it checks if the number is divisible by any number from 2 to the square root of the number, if it is, then it's not a prime number. If none of these conditions are met, then the number is a prime number.

In the `xOrY` function, we call the `isPrime` function with the number `n` as the parameter. If `isPrime` returns `true`, then `n` is a prime number and we return the value of `x`. Otherwise, we return the value of `y`.