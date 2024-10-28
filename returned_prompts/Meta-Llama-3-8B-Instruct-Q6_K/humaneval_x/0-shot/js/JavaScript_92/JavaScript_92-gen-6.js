The solution is:
```javascript
const anyInt = (x, y, z) => {
  if (isNaN(x) || isNaN(y) || isNaN(z)) return false;
  if (x + y === z || x + z === y || y + z === x) return true;
  return false;
};
```
Explanation:

* We first check if any of the numbers are not integers using `isNaN()`. If any of them are not integers, we return `false`.
* Then we check if the sum of any two numbers is equal to the third number. We do this by checking if `x + y === z`, `x + z === y`, or `y + z === x`. If any of these conditions are true, we return `true`.
* If none of the above conditions are true, we return `false`. This means that none of the numbers are equal to the sum of the other two, so we return `false`.