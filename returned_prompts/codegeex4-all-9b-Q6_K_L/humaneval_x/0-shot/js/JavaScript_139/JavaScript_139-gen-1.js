You can solve this problem by using a recursive approach. The function should recursively call itself with the argument decreased by 1 until it reaches 1. The special factorial can be calculated by multiplying the current number with the result of the recursive call. Here's the solution:

```javascript
const specialFactorial = (n) => {
  if (n === 1) {
    return 1;
  }
  return n * specialFactorial(n - 1);
};
```

In this solution, we first check if the input number is 1. If it is, we return 1 as the base case for the recursion. Otherwise, we return the product of the current number and the result of the recursive call with the argument decreased by 1. This will continue until we reach the base case and the recursion stops.

The time complexity of this solution is O(n) because we are making n recursive calls.