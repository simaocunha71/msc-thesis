To solve this problem, you can use a recursive approach. The base case of the recursion is when `n` is equal to 1, in which case the function should return 1. For any other value of `n`, the function should return the product of `n` and the result of the function call with `n-1`.

Here's the updated code:

```javascript
const specialFactorial = (n) => {
  if (n === 1) {
    return 1;
  } else {
    return n * specialFactorial(n - 1);
  }
};
```

This code should correctly calculate the special factorial of a given integer.