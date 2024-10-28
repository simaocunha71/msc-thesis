You can use the built-in `Math.round()` function in JavaScript to round a number to the nearest integer. This function will return the value rounded up if the decimal part is .5 or greater, and rounded down otherwise. Here is how you can implement this:

```javascript
const closestInteger = (value) => {
  return Math.round(parseFloat(value));
}
```

The `parseFloat()` function is used to convert the string value to a number before applying `Math.round()`.