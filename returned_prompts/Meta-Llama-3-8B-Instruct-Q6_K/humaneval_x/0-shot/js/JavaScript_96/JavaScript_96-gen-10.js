Here is the implementation in JavaScript:

```javascript
const countUpTo = (n) => {
  const primes = [];
  for (let i = 2; i < n; i++) {
    if (isPrime(i)) {
      primes.push(i);
    }
    if (primes.length === n - 1) {
      break;
    }
  }
  return primes;
};

const isPrime = (num) => {
  if (num <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```

In this code, the function `countUpTo` generates an array of prime numbers less than `n`. It does this by iterating over the numbers from 2 to `n-1` and checking if each number is prime using the `isPrime` function. If a number is prime, it is added to the `primes` array. The loop stops once the `primes` array has `n-1` elements, or once it has checked all numbers up to `n-1`.

The `isPrime` function checks if a number is prime by testing if it has any divisors other than 1 and itself. It does this by iterating over the numbers from 2 to the square root of the number, and checking if the number is divisible by any of these. If it finds a divisor, it returns `false`. If it doesn't find any divisors, it returns `true`.