Here is a solution that uses the `Math.round()` function to round the value to the nearest integer, and then checks if the value is equidistant from two integers. If it is, it rounds away from zero.

```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  const rounded = Math.round(num);
  if (Math.abs(num - rounded) === Math.abs(num - rounded - 1)) {
    return rounded + 1;
  }
  return rounded;
};
```

This function first converts the input value to a number using `parseFloat()`. It then uses `Math.round()` to round the value to the nearest integer.

If the absolute difference between the original value and the rounded value is equal to the absolute difference between the original value and the rounded value minus 1, it means that the original value is equidistant from two integers. In this case, the function returns the integer that is farther away from zero.

If the original value is not equidistant from two integers, the function simply returns the rounded value.