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
  if (n <= 1) return false;
  for (let i = 2, sqrt = Math.sqrt(n); i <= sqrt; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```


The code defines a function `primeFib` that returns the `n-th` Fibonacci number that is also a prime number. It uses a helper function `isPrime` to check if a number is prime.

In the `primeFib` function, we initialize two variables `a` and `b` to the first two Fibonacci numbers, and a `count` variable to keep track of the number of prime Fibonacci numbers found.

The function then enters an infinite loop, where it generates the next Fibonacci number `fib` by adding `a` and `b`, and updates `a` and `b` to the new values. If `fib` is a prime number, it increments the `count` variable and checks if it's equal to `n`. If it is, the function returns `fib`.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of the iteration values. If it is, the function returns `false`. Otherwise, it returns `true`.

This code can be optimized by using a more efficient primality test, such as the Miller-Rabin primality test, or by using a lookup table to store previously computed prime Fibonacci numbers. However, for small values of `n`, the code should be sufficient.