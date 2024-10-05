  let factors = [];

  // Check for 2s
  while (n % 2 === 0) {
    factors.push(2);
    n /= 2;
  }

  // Check for odd factors
  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i === 0) {
      factors.push(i);
      n /= i;
    }
  }

  // Check for remaining prime
  if (n > 2) {
    factors.push(n);
  }

  return factors;
}

console.log(factorize(8));
console.log(factorize(25));
console.log(factorize(70));
```

##### JavaScript: Fibonacci Sequence

```javascript
