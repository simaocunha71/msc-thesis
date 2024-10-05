Here is one way to solve the problem:

```javascript
const isMultiplyPrime = (a) => {
  // Check if the number is less than 100
  if (a < 100) {
    // Check if the number is a multiplication of 3 prime numbers
    const factors = primeFactors(a);
    if (factors.length === 3) {
      return factors.every(isPrime);
    }
  }
  return false;
}

const primeFactors = (n) => {
  let factors = [];
  for (let i = 2; i <= Math.sqrt(n); i++) {
    while (n % i === 0) {
      factors.push(i);
      n /= i;
    }
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}

const isPrime = (n) => {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}
```

The `isMultiplyPrime` function checks if the given number is less than 100 and if it is, it calculates the prime factors of the number using the `primeFactors` function. If the number of prime factors is 3, it checks if all of them are prime using the `isPrime` function. If all of them are prime, it returns true, otherwise it returns false.