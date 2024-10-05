You can solve this problem using the `Math.round()` function in JavaScript. Here's the implementation:

```javascript
const closestInteger = (value) => {
  return Math.round(parseFloat(value));
};
```

This function takes a string `value` as input, converts it to a float using `parseFloat()`, and then rounds it to the nearest integer using `Math.round()`. Finally, it returns the rounded integer.