```js
const countUpTo = (n) => {
  let primes = [];
  let i = 2;
  while (primes.length < n) {
    if (isPrime(i)) {
      primes.push(i);
    }
    i++;
  }
  return primes;
};

const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2; i < num; i++) {
    if (num % i === 0) return false;
  }
  return true;
};
```
Explanation:
We start with the smallest prime number, 2, and keep adding prime numbers to the `primes` array until we reach `n` prime numbers. We use the `isPrime` function to check if a number is prime. If a number is prime, we add it to the `primes` array. If a number is not prime, we continue to the next number. We continue this process until we reach `n` prime numbers. Finally, we return the `primes` array.