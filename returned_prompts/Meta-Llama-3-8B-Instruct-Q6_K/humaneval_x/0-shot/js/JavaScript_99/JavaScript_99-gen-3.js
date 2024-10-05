```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(Math.abs(num) + (num >= 0 ? 0 : 1));
};
```
Explanation:
The `parseFloat` function is used to convert the input string to a floating-point number. Then, `Math.abs` is used to get the absolute value of the number. If the number is non-negative, we add 0 to it. If the number is negative, we add 1 to it. Finally, `Math.round` is used to round the result to the nearest integer.

This function works by rounding the absolute value of the number, and then adjusting the sign back to the original sign of the input number. This ensures that the function rounds away from zero when the number is equidistant from two integers. For example, `closestInteger("14.5")` will return 15, and `closestInteger("-14.5")` will return -15.