```javascript
const truncateNumber = (number) => {
  return number - Math.floor(number);
};
```
Explanation:
In this problem, we need to return the decimal part of a given floating point number. We can do this by subtracting the integer part from the original number. The integer part is obtained using the `Math.floor()` function, which returns the largest integer smaller than or equal to the given number.

For example, if we have `3.5`, `Math.floor(3.5)` returns `3`, so `3.5 - 3 = 0.5`, which is the decimal part.

This solution works for all positive floating point numbers. For example, `truncateNumber(3.5)` returns `0.5`, `truncateNumber(1.23)` returns `0.23`, and so on.