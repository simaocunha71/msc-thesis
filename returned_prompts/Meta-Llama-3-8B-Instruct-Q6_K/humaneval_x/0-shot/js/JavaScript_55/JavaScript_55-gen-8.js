```javascript
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  let a = 1;
  let b = 1;
  for (let i = 2; i < n; i++) {
    const sum = a + b;
    a = b;
    b = sum;
  }
  return b;
};
```


The solution is a simple implementation of the Fibonacci sequence, where we calculate the `n-th` number by maintaining the previous two numbers in the sequence, `a` and `b`, and updating them iteratively. The base case is when `n` is less than or equal to 1, in which case we return `n` itself.

This function works correctly for positive integers `n`, but it would be more robust to add error handling for non-integer or negative inputs. For example, you could use a `try`-`catch` block to return an error message for invalid inputs.

Here's an updated version of the function with error handling:
```javascript
const fib = (n) => {
  if (typeof n !== 'number') {
    throw new Error('Input must be a number');
  }
  if (n < 1) {
    throw new Error('Input must be a positive integer');
  }
  if (n === 1) {
    return 1;
  }
  let a = 1;
  let b = 1;
  for (let i = 2; i < n; i++) {
    const sum = a + b;
    a = b;
    b = sum;
  }
  return b;
};
```
This function will throw an error if the input is not a positive integer, and return the correct Fibonacci number for valid inputs.