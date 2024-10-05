You can solve this problem by using the `Math.round()` function in JavaScript. This function rounds a number to the nearest integer. If the number is equidistant from two integers, it rounds it away from zero.

Here is the code:

```javascript
const closestInteger = (value) => {
  return Math.round(value);
};
```

This code will take the input `value` and round it to the nearest integer using `Math.round()`.