```javascript
const isMultiplyPrime = (a) => {
  for (let i = 2; i <= a; i++) {
    if (isPrime(i) && isPrime(a / i) && a % i === 0) {
      return true;
    }
  }
  return false;
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```

The function `isMultiplyPrime` takes an integer `a` as input. It checks if `a` is the multiplication of 3 prime numbers. If it finds 3 prime numbers that multiply to `a`, it returns `true`. If no such combination is found, it returns `false`.

The helper function `isPrime` checks if a number `n` is prime. It does this by checking if `n` is divisible by any number from 2 to the square root of `n`. If `n` is divisible by any of these numbers, it is not prime. If `n` is not divisible by any of these numbers, it is prime.

The `isMultiplyPrime` function iterates over all numbers from 2 to `a`. For each number `i`, it checks if `i` is prime, if `a / i` is prime, and if `a` is divisible by `i`. If all these conditions are true, it returns `true`. If it iterates over all numbers without finding a combination that satisfies these conditions, it returns `false`.