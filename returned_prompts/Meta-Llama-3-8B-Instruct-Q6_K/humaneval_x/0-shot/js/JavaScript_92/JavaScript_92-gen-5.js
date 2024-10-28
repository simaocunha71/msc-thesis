```javascript
const anyInt = (x, y, z) => {
  if (!Number.isInteger(x) || !Number.isInteger(y) || !Number.isInteger(z)) {
    return false;
  }
  return (x === y + z) || (x === z + y) || (y === x + z) || (y === z + x) || (z === x + y) || (z === y + x);
};
``` A) The function `anyInt` takes three numbers `x`, `y`, and `z` as arguments. It first checks if all three numbers are integers using the `Number.isInteger` method. If any of the numbers is not an integer, the function immediately returns `false`. If all numbers are integers, the function then checks if one of the numbers is equal to the sum of the other two using six different conditional expressions. If any of these conditions is true, the function returns `true`; otherwise, it returns `false`. This ensures that the function returns `true` only when one of the numbers is equal to the sum of the other two, and all numbers are integers.