```js
const primeFib = (n) => {
  let fib = [0, 1];
  let primes = [2];

  while (primes.length < n) {
    fib.push(fib[fib.length - 1] + fib[fib.length - 2]);
    let nextFib = fib[fib.length - 1];

    for (let i = 2; i < Math.sqrt(nextFib) + 1; i++) {
      if (nextFib % i === 0) {
        break;
      }
      if (i === Math.floor(Math.sqrt(nextFib))) {
        primes.push(nextFib);
      }
    }
  }

  return primes[primes.length - 1];
}
```
