```javascript
const fib = (n) => {
  if (n <= 1) return n;
  let a = 0, b = 1, result = 1;
  for (let i = 2; i <= n; i++) {
    [a, b] = [b, a + b];
  }
  return b;
};
```
Explanation:
This function calculates the nth Fibonacci number using a loop. The Fibonacci sequence is defined as a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

The function first checks if `n` is less than or equal to 1, in which case it returns `n` because the 0th and 1st Fibonacci numbers are 0 and 1, respectively.

Then, it initializes three variables: `a` to 0, `b` to 1, and `result` to 1. These variables are used to keep track of the previous two Fibonacci numbers and the current result, respectively.

The loop starts from 2 and goes up to `n`. In each iteration, it updates `a` and `b` to `b` and `a + b`, respectively. This effectively calculates the next Fibonacci number in the sequence.

Finally, the function returns `b`, which is the `n`th Fibonacci number.

This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large values of `n`.