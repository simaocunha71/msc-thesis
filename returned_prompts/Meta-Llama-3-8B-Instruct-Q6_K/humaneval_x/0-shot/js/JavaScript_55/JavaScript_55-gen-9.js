```javascript
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  let a = 0;
  let b = 1;
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
};
```


This code defines a function `fib` that takes an integer `n` as input and returns the `n`-th Fibonacci number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

The function uses a for loop to iterate from 2 to `n`, and in each iteration, it calculates the next Fibonacci number as the sum of the previous two numbers, stored in the variables `a` and `b`. The `result` variable keeps track of the current Fibonacci number.

The base case is handled by returning `n` if `n` is less than or equal to 1, since the Fibonacci sequence starts with 0 and 1.

The function returns the final value of `result`, which is the `n`-th Fibonacci number. For example, `fib(10)` returns 55, `fib(1)` returns 1, and `fib(8)` returns 21.