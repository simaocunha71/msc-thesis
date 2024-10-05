Here is a JavaScript solution for the problem:

```javascript
const isMultiplyPrime = (a) => {
  let count = 0;
  let primes = [];
  for (let i = 2; i <= a; i++) {
    if (isPrime(i)) {
      primes.push(i);
      if (primes.length === 3) {
        if (a % (primes[0] * primes[1] * primes[2]) === 0) {
          return true;
        }
        primes = [];
      }
    }
  }
  return false;

  function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
      if (n % i === 0) return false;
    }
    return true;
  }
};
```

In this solution, we first define a helper function `isPrime` that checks whether a number is prime or not. Then, we iterate through all numbers from 2 to `a` and check if each number is prime. If a prime number is found, we add it to our array of primes. If the length of our array of primes reaches 3, we check if `a` is a multiple of the product of the three primes. If it is, we return `true`. If we finish iterating through all numbers and haven't found a combination of three primes that multiply to `a`, we return `false`.