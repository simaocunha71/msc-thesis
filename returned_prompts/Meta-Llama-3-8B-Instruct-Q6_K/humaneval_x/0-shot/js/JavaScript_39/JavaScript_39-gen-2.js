```
const primeFib = (n) => {
  let a = 0, b = 1, count = 0;
  while (true) {
    const fib = a + b;
    a = b;
    b = fib;
    if (isPrime(fib)) {
      count++;
      if (count === n) return fib;
    }
  }
};

const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```