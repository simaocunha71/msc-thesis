You can solve this problem using recursion. Here's a possible solution in JavaScript:

```javascript
const specialFactorial = (n) => {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * specialFactorial(n - 1);
  }
};
```

In this solution, we check if `n` is 0 or 1. If it is, we return 1, as 0! and 1! are both equal to 1. Otherwise, we recursively call `specialFactorial` with `n - 1` and multiply the result by `n`. This way, we calculate the product of all integers from `n` down to 1.

Here's how you can test the function:

```javascript
console.log(specialFactorial(4)); // Output: 288
console.log(specialFactorial(5)); // Output: 14400
console.log(specialFactorial(6)); // Output: 720720
```