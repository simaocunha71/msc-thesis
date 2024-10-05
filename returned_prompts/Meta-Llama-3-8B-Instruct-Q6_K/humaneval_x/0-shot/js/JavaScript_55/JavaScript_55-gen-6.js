Here is the solution for the problem. This function uses recursion to calculate the n-th Fibonacci number.

```javascript
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
};
```

This function works by recursively calling itself with smaller values of n until it reaches the base cases of n <= 1. At this point, it returns the value of n. The function then adds up the results of the recursive calls to calculate the n-th Fibonacci number.

However, please note that this recursive approach can be inefficient and may cause a stack overflow for large values of n. For a more efficient solution, you can use an iterative approach or a memoized recursive approach.

Here is an example of a memoized recursive approach:

```javascript
const memo = {};

const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  if (memo[n]) {
    return memo[n];
  }
  const result = fib(n - 1) + fib(n - 2);
  memo[n] = result;
  return result;
};
```

This approach uses a memoization object to store the results of previously computed Fibonacci numbers. This allows the function to avoid recomputing the same values multiple times, making it more efficient for larger values of n.