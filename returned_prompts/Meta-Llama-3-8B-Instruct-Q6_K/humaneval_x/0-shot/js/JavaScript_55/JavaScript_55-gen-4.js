```javascript
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  let a = 0;
  let b = 1;
  for (let i = 2; i <= n; i++) {
    const temp = a + b;
    a = b;
    b = temp;
  }
  return b;
};
```
This function calculates the n-th Fibonacci number using a simple iterative approach. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, usually starting with 0 and 1.

The function first checks if `n` is less than or equal to 1, in which case it returns `n` directly, since the first two Fibonacci numbers are 0 and 1.

Then it initializes two variables `a` and `b` to 0 and 1, respectively, which represent the previous two Fibonacci numbers. It then enters a loop that runs from `i = 2` to `i = n`. In each iteration, it calculates the next Fibonacci number `temp` as the sum of `a` and `b`, and then updates `a` and `b` to `b` and `temp`, respectively.

Finally, it returns the `n-th` Fibonacci number, which is stored in `b`. This approach has a time complexity of O(n) and a space complexity of O(1), making it efficient for calculating large Fibonacci numbers.