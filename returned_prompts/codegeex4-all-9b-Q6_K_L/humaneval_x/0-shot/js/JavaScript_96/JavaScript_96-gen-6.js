Here's one way you can implement the `countUpTo` function in JavaScript:

```javascript
const countUpTo = (n) => {
  const primes = [];
  for (let i = 2; i < n; i++) {
    let isPrime = true;
    for (let j = 2; j <= Math.sqrt(i); j++) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primes.push(i);
    }
  }
  return primes;
}
```

This function first initializes an empty array `primes` to store the prime numbers. Then it iterates from 2 to `n-1` (since 1 is not a prime number). For each number `i`, it checks if it is prime by iterating from 2 to the square root of `i` (since if `i` is not prime, it will have a factor less than or equal to its square root). If `i` is not divisible by any number in this range, it is prime and is added to the `primes` array. Finally, the function returns the `primes` array.