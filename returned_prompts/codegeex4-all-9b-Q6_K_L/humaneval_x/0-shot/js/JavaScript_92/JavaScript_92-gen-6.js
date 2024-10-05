You can create a function that checks if any of the numbers is equal to the sum of the other two, and also checks if all numbers are integers. Here's how you can do it:

```javascript
const anyInt = (x, y, z) => {
  // Check if all numbers are integers
  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) {
    return false;
  }
  // Check if one of the numbers is equal to the sum of the other two
  if (x === y + z || y === x + z || z === x + y) {
    return true;
  }
  return false;
};
```

This function first checks if all numbers are integers using the `Number.isInteger()` method. If any of the numbers is not an integer, it immediately returns false.

Then it checks if one of the numbers is equal to the sum of the other two. If any of these conditions is true, it returns true. Otherwise, it returns false.

You can test the function with the provided examples:

```javascript
console.log(anyInt(5, 2, 7)); // true
console.log(anyInt(3, 2, 2)); // false
console.log(anyInt(3, -2, 1)); // true
console.log(anyInt(3.6, -2.2, 2)); // false
```

This function will work correctly for the given examples and should return the expected results.