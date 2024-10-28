```javascript
const anyInt = (x, y, z) => {
  if (isNaN(x) || isNaN(y) || isNaN(z)) return false;
  return (x === y + z || x === z + y || y === x + z || y === z + x || z === x + y || z === y + x);
};
```


Explanation:

The function `anyInt` takes three numbers as arguments. It first checks if any of the numbers is not a valid integer (NaN) by using the `isNaN()` function. If any of the numbers is not a valid integer, it immediately returns `false`.

If all numbers are valid integers, it then checks if one of the numbers is equal to the sum of the other two by using the `===` operator. It checks all possible combinations of numbers (x === y + z, x === z + y, y === x + z, y === z + x, z === x + y, z === y + x) and returns `true` if any of these conditions is met.

If none of the conditions is met, it returns `false`. This ensures that the function returns `true` only if one of the numbers is equal to the sum of the other two, and all numbers are integers.