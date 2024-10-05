You can use the following approach:

1. Create a helper function to check if a number is prime.
2. Create a helper function to find the prime factors of a number.
3. In the main function, use the helper functions to find the prime factors of the given number.
4. If the length of the prime factors array is 3, return true; otherwise, return false.

Here is the implementation in JavaScript:

```javascript
const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const primeFactors = (num) => {
  const factors = [];
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (isPrime(i) && num % i === 0) {
      factors.push(i);
      num /= i;
    }
  }
  if (num > 1) {
    factors.push(num);
  }
  return factors;
};

const isMultiplyPrime = (a) => {
  const factors = primeFactors(a);
  return factors.length === 3;
};

console.log(isMultiplyPrime(30)); // true
console.log(isMultiplyPrime(27)); // false
```

This code first checks if a number is prime using the `isPrime` function. Then, it finds the prime factors of a number using the `primeFactors` function. Finally, it checks if the length of the prime factors array is 3 using the `isMultiplyPrime` function.