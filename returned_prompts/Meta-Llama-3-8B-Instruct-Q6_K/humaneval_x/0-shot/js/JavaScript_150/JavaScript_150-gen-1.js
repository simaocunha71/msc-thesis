```
function xOrY(n, x, y) {
  if (isPrime(n)) {
    return x;
  } else {
    return y;
  }
}

function isPrime(num) {
  if (num <= 1) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}
```



Explanation:
The `xOrY` function takes three parameters, `n`, `x`, and `y`. It checks if `n` is a prime number using the `isPrime` function. If `n` is a prime number, it returns the value of `x`. If `n` is not a prime number, it returns the value of `y`.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the iterated values. If the number is divisible, it returns `false`, indicating that the number is not prime. If the number is not divisible by any of the iterated values, it returns `true`, indicating that the number is prime.

In the examples provided, `xOrY(7, 34, 12)` returns `34` because 7 is a prime number, and `xOrY(15, 8, 5)` returns `5` because 15 is not a prime number.