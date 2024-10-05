```
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```


In this solution, we use the `parseFloat` function to convert the given string to a floating-point number, and then use the `Math.round` function to round it to the nearest integer. This ensures that if the number is equidistant from two integers, it will be rounded away from zero.

For example, if the input is "10", `parseFloat` will convert it to the number 10, and `Math.round` will return the same number 10. If the input is "15.3", `parseFloat` will convert it to the number 15.3, and `Math.round` will return the integer 15.

This solution meets the requirements of the problem, as it correctly rounds the given number to the nearest integer, and rounds away from zero when the number is equidistant from two integers.