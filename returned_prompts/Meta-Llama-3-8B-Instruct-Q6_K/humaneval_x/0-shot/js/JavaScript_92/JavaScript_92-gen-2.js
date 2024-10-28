```javascript
const anyInt = (x, y, z) => {
  if (isNaN(x) || isNaN(y) || isNaN(z)) return false;
  return (x + y === z) || (x + z === y) || (y + z === x);
};
```
Explanation:
The function `anyInt` takes three numbers `x`, `y`, and `z` as arguments. It first checks if any of the numbers are not integers (i.e., `NaN` or not a number) using the `isNaN` function. If any of the numbers are not integers, it returns `false`.

If all numbers are integers, it then checks if one of the numbers is equal to the sum of the other two using the `||` operator. It checks for three possible combinations: `x + y === z`, `x + z === y`, and `y + z === x`. If any of these combinations is true, it returns `true`. Otherwise, it returns `false`.