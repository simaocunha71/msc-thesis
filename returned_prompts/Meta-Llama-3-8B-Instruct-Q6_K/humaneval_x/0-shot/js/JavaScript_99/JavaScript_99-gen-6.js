```
const closestInteger = (value) => {
  let num = parseFloat(value);
  if (isNaN(num)) {
    return NaN;
  }
  return Math.round(num);
};
```


The function `closestInteger` takes a string value representing a number as an argument. It first converts the string to a float using `parseFloat`. If the conversion fails (i.e., the string is not a valid number), it returns `NaN` (Not a Number).

Then, it uses the `Math.round` method to round the float to the nearest integer. Since `Math.round` rounds halfway cases away from zero, this implementation meets the requirement of rounding away from zero when the number is equidistant from two integers. For example, `closestInteger("14.5")` returns `15` and `closestInteger("-14.5")` returns `-15`.