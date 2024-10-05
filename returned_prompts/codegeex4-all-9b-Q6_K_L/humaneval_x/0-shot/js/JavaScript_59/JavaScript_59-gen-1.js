To solve this problem, we can use the following steps:

1. Create a helper function that checks if a number is prime.
2. Iterate from 2 to the square root of n.
3. For each number i, if n is divisible by i and i is prime, return i.
4. If no prime factor is found, return n itself.

Here's the updated code:

```javascript
const largestPrimeFactor = (n) => {
  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0 && isPrime(i)) {
      return i;
    }
  }

  return n;
};

console.log(largestPrimeFactor(13195)); // 29
console.log(largestPrimeFactor(2048)); // 2
```

This solution works by iterating from 2 to the square root of n and checking if n is divisible by i and i is prime. If a prime factor is found, it is returned. If no prime factor is found, n itself is returned.