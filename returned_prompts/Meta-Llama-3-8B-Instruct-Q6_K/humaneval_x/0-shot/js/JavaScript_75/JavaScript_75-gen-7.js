```javascript
const isMultiplyPrime = (a) => {
  function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++)
      if (n % i === 0) return false;
    return true;
  }

  for (let i = 2; i <= 100; i++) {
    for (let j = i; j <= 100; j++) {
      for (let k = j; k <= 100; k++) {
        if (i * j * k === a && isPrime(i) && isPrime(j) && isPrime(k)) {
          return true;
        }
      }
    }
  }
  return false;
};
```


This code defines a function `isMultiplyPrime` that takes an integer `a` as input. It first defines a helper function `isPrime` to check if a number is prime.

The main function then iterates over all possible combinations of three numbers between 2 and 100, checks if their product is equal to `a`, and if all three numbers are prime. If such a combination is found, the function returns `true`. If no such combination is found after checking all possibilities, the function returns `false`.