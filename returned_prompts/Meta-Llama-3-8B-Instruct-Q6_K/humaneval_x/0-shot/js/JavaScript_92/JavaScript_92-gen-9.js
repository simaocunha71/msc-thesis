```javascript
const anyInt = (x, y, z) => {
  if (Number.isInteger(x) && Number.isInteger(y) && Number.isInteger(z)) {
    return (x === y + z) || (x === z + y) || (y === x + z) || (y === z + x) || (z === x + y) || (z === y + x);
  }
  return false;
};
```


Explanation:
The function `anyInt` takes three numbers as arguments. It first checks if all three numbers are integers using `Number.isInteger()`. If they are not integers, it returns `false`.

If they are integers, it checks if one of the numbers is equal to the sum of the other two. It does this by using three pairs of conditional statements to check for each possible combination of numbers. If any of these conditions are true, it returns `true`.

If none of the conditions are true, it returns `false`. This ensures that the function returns `true` only if one of the numbers is equal to the sum of the other two, and all numbers are integers.