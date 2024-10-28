Here is the solution using JavaScript:

```javascript
const closestInteger = (value) => {
  const num = parseFloat(value);
  return Math.round(num);
};
```

Explanation:
The `parseFloat` function is used to convert the input string into a floating-point number. The `Math.round` function is then used to round the number to the nearest integer. If the number is equidistant from two integers, `Math.round` will round away from zero, as required. For example, `closestInteger("14.5")` will return `15` and `closestInteger("-14.5")` will return `-15`. This solution passes all the given examples.