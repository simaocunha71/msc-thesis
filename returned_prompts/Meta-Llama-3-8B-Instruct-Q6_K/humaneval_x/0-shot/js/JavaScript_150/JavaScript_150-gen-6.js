```
const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const xOrY = (n, x, y) => {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
};
```
The code above first defines a helper function `isPrime` to check if a number is prime. This function works by checking if the number is less than or equal to 1 (in which case it is not prime), or if it has any divisors other than 1 and itself (in which case it is not prime). If the number passes these checks, it is considered prime.

The `xOrY` function then uses the `isPrime` function to determine if `n` is prime. If it is, it returns `x`, otherwise it returns `y`. This function can be used to check if a number is prime and return a value based on the result. For example, if we call `xOrY(7, 34, 12)`, it will return `34` because 7 is a prime number. If we call `xOrY(15, 8, 5)`, it will return `5` because 15 is not a prime number.