```js
const primeFib = (n) => {
  const isPrime = (num) => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  const fib = (n) => {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
  };

  let count = 0;
  let i = 0;
  while (count < n) {
    let fibNum = fib(i);
    if (isPrime(fibNum)) {
      count++;
    }
    i++;
  }
  return fib(i - 1);
};
```