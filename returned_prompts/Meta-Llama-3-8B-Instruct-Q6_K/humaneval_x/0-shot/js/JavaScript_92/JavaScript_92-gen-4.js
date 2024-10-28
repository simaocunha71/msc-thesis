```javascript
const anyInt = (x, y, z) => {
  // Check if all numbers are integers
  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) {
    return false;
  }
  // Check if one of the numbers is equal to the sum of the other two
  return (x + y === z) || (x + z === y) || (y + z === x);
};
```


Explanation:
1. First, we check if all numbers are integers by using the `Number.isInteger()` method. If any of the numbers is not an integer, we return `false`.
2. If all numbers are integers, we then check if one of the numbers is equal to the sum of the other two. We do this by using three conditional statements that check if the sum of two numbers is equal to the third number.
3. If any of these conditions are true, we return `true`. Otherwise, we return `false`.