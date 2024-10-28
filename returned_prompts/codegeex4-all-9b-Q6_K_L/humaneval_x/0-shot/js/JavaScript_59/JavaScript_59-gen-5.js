```javascript
  const factors = [];
  for (let i = 2; i <= n; i++) {
    if (n % i === 0) factors.push(i);
  }

  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  for (let i = factors.length - 1; i >= 0; i--) {
    if (isPrime(factors[i])) return factors[i];
  }
};
```
