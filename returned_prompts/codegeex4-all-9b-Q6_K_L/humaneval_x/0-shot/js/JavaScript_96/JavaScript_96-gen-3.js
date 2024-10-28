```javascript
const countUpTo = (n) => {
  let primes = [];
  let isPrime = true;
  for (let i = 2; i < n; i++) {
    for (let j = 2; j < i; j++) {
      if (i % j === 0) {
        isPrime = false;
        break;
      }
    }
    if (isPrime) {
      primes.push(i);
    }
    isPrime = true;
  }
  return primes;
}
```

Explanation:
1. Initialize an empty array called `primes` to store the prime numbers.
2. Initialize a boolean variable called `isPrime` to `true` to keep track of whether a number is prime or not.
3. Loop from 2 to `n-1` (since we are looking for prime numbers less than `n`).
4. For each number, loop from 2 to `i-1` to check if `i` is divisible by any number in that range.
5. If `i` is divisible by any number in the range, set `isPrime` to `false` and break out of the loop.
6. If `isPrime` is still `true` after the inner loop, push `i` to the `primes` array.
7. Finally, return the `primes` array.