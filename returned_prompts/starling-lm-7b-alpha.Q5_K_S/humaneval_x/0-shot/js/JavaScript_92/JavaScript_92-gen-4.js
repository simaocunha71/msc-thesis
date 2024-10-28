To solve this kata, you'll need to check if one of the numbers is equal to the sum of the other two. However, this alone won't be enough to solve the problem because the numbers can be any combination of positive and negative numbers. To determine if a number is an integer, you can use the `Number.isInteger()` method. The `Number.isInteger()` method returns `true` if the number is an integer and `false` if it is not.

Here's a step-by-step solution:

1. Define the `anyInt` function that takes three arguments: `x`, `y`, and `z`.
2. Check if `x` is equal to the sum of `y` and `z` using the `===` operator. If it is, return `true`.
3. If `x` is not equal to the sum of `y` and `z`, check if `y` is equal to the sum of `x` and `z`. If it is, return `true`.
4. If neither `x` nor `y` is equal to the sum of the other two, check if `z` is equal to the sum of `x` and `y`. If it is, return `true`.
5. If none of the conditions above are met, return `false`.
6. Call the `Number.isInteger()` method on each number to ensure that they are integers. If any of the numbers is not an integer, return `false`.
7. If all the numbers are integers and one of them is equal to the sum of the other two, return `true`. Otherwise, return `false`.

Here's the code for the solution:
```javascript
const anyInt = (x, y, z) => {
  if (x === y + z || y === x + z || z === x + y) {
    if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
      return true;
    }
  }
  return false;
};
```

You can test the function with the provided examples:
```javascript
console.log(anyInt(5, 2, 7));  // true
console.log(anyInt(3, 2, 2