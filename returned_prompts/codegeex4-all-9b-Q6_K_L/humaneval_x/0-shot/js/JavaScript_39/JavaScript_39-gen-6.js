Here's how you might define the `primeFib` function in JavaScript:

```javascript
const primeFib = (n) => {
  let count = 0;
  let a = 1;
  let b = 1;

  const isPrime = (num) => {
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return num > 1;
  }

  while (count < n) {
    let next = a + b;
    a = b;
    b = next;
    if (isPrime(next)) {
      count++;
    }
  }

  return a;
}
```

In this function, we first define a helper function `isPrime` that checks whether a given number is prime.

We then use a loop to generate Fibonacci numbers. For each number, we check if it's prime. If it is, we increment a counter. When the counter reaches `n`, we return the current Fibonacci number, which is the `n`-th prime Fibonacci number.