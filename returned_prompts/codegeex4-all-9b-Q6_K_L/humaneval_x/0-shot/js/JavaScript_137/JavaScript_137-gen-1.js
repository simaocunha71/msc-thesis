You can solve this problem by using the `parseFloat()` function to convert any string argument to a number. Then, you can simply compare the two numbers to determine the larger one. Here is the solution:

```javascript
const compareOne = (a, b) => {
  const numA = parseFloat(a);
  const numB = parseFloat(b);

  if (numA === numB) {
    return null;
  } else if (numA > numB) {
    return a;
  } else {
    return b;
  }
};
```

This solution works for integers, floats, and strings representing real numbers. If the values are equal, it returns `null`.