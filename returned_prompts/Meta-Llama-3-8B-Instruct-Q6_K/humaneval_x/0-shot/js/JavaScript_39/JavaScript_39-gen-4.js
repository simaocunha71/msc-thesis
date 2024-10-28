Here is the implementation of the `primeFib` function in JavaScript:
```
const primeFib = (n) => {
  let a = 0, b = 1, count = 0;
  while (true) {
    const fib = a + b;
    a = b;
    b = fib;
    if (isPrime(fib)) {
      count++;
      if (count === n) {
        return fib;
      }
    }
  }
};

const isPrime = (n) => {
  if (n <= 1) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
};
```
This implementation uses a simple iterative approach to generate Fibonacci numbers and a helper function `isPrime` to check if a number is prime.

The `primeFib` function starts with `a = 0` and `b = 1`, which are the first two Fibonacci numbers. It then enters a loop where it calculates the next Fibonacci number as `a + b`, updates `a` and `b` to the new values, and checks if the new Fibonacci number is prime using the `isPrime` function. If it is prime, it increments a counter `count`. When `count` reaches `n`, it returns the current Fibonacci number.

The `isPrime` function is a simple trial division algorithm that checks if a number is prime by dividing it by all numbers up to its square root. If the number is not divisible by any of these numbers, it is prime.

You can test the `primeFib` function with different values of `n` to see the expected results. For example:
```
console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13
console.log(primeFib(5)); // 89
``` 