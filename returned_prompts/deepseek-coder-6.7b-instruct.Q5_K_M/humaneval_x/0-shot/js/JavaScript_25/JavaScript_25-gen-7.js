  const factors = [];

  for (let divisor = 2; n > 1; divisor++) {
    while (n % divisor === 0) {
      factors.push(divisor);
      n /= divisor;
    }
  }

  return factors;
}

console.log(factorize(8));  // [2, 2, 2]
console.log(factorize(25)); // [5, 5]
console.log(factorize(70)); // [2, 5, 7]

// 1. Create an empty array factors
// 2. Start a loop from 2 to n
// 3. Within the loop, while n is divisible by the divisor, push the divisor to the factors array and divide n by the divisor
// 4. Return the factors array
```

## Code: Sieve of Eratosthenes

```javascript
