```javascript
const isPrime = (num) => {
  if (num < 2) return false;
  for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const fibonacci = (n) => {
  let [a, b] = [0, 1];
  let count = 0;
  while (count < n) {
    [a, b] = [b, a + b];
    if (isPrime(b)) count++;
  }
  return b;
};

const primeFib = (n) => {
  return fibonacci(n);
};

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
```A

The code defines two helper functions: `isPrime` checks if a number is prime, and `fibonacci` generates Fibonacci numbers until it finds the `n`-th prime Fibonacci number. The `primeFib` function simply calls `fibonacci` with the given `n` as an argument.

In the `fibonacci` function, we use a loop to generate Fibonacci numbers, and for each number, we check if it's prime using the `isPrime` function. If it's prime, we increment a counter. When the counter reaches `n`, we return the current Fibonacci number.

Note that this implementation has a time complexity of O(n^2) due to the nested loops in the `isPrime` function. For large values of `n`, this may be slow. A more efficient implementation could use a sieve to generate prime numbers up to a certain limit, or use a more advanced primality test.