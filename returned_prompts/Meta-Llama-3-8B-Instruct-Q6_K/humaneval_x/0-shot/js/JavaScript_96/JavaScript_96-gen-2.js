Here is a JavaScript function that implements the described behavior:

```javascript
function countUpTo(n) {
  if (n < 1) {
    return [];
  }

  const primes = [];
  let num = 2;

  while (num < n) {
    if (isPrime(num)) {
      primes.push(num);
    }
    num++;
  }

  return primes;
}

function isPrime(num) {
  if (num < 2) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}
```

In this code, the `countUpTo` function generates the first n prime numbers and returns them as an array. The `isPrime` function is used to check whether a given number is prime or not. It does this by checking if the number is divisible by any number up to its square root. If it is divisible, it's not a prime number. If it's not divisible by any of those numbers, it's a prime number. The `countUpTo` function uses this `isPrime` function to filter out non-prime numbers and only include prime numbers in the returned array.

This code works correctly for all non-negative integers, including 0 and 1. For 0 and 1, it returns an empty array as expected. For all other numbers, it returns an array of the first n prime numbers that are less than n. For example, `countUpTo(5)` returns `[2, 3]`, `countUpTo(11)` returns `[2, 3, 5, 7]`, and so on.