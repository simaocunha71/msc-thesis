```javascript
function fib(n) {
  if (n <= 1) {
    return n;
  }
  let a = 0, b = 1, result = 1;
  for (let i = 2; i <= n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}
```


Explanation:
The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. In this code, we define a function `fib(n)` that takes an integer `n` as input and returns the `n`-th Fibonacci number.

We use a simple iterative approach to calculate the Fibonacci number. We initialize three variables: `a` and `b` to the first two Fibonacci numbers (0 and 1), and `result` to the first Fibonacci number (1).

We then loop from 2 to `n`, updating `result` to be the sum of `a` and `b`, and updating `a` and `b` to be the previous values of `result` and `a`, respectively.

Finally, we return the `result`, which is the `n`-th Fibonacci number.

This code works for any positive integer `n`, and it is efficient because it only requires a constant amount of memory and a linear amount of time.