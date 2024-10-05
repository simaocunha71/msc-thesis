```javascript
const anyInt = (x, y, z) => {
  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) {
    return false;
  }
  return x === y + z || x === z + y || y === x + z || y === z + x || z === x + y || z === y + x;
};
```
The code defines a function `anyInt` that takes three numbers as arguments. It first checks if all the numbers are integers using the `Number.isInteger` method. If any of the numbers are not integers, the function returns `false`.

If all the numbers are integers, the function then checks if one of the numbers is equal to the sum of the other two. It does this by checking all possible combinations of the three numbers and returns `true` if any of these combinations is true. Otherwise, it returns `false`.

The function is tested with the examples provided in the problem statement, and it returns the expected results.