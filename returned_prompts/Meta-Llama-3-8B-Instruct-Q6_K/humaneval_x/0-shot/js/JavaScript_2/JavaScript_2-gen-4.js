```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
};
```
The `Math.floor()` function is used to get the largest integer smaller than the given number. By subtracting this integer from the original number, we get the decimal part.

Example:
```javascript
console.log(truncateNumber(3.5)); // Output: 0.5
```
This code works because `Math.floor(3.5)` returns `3`, and `3.5 - 3` equals `0.5`. The decimal part is then returned.