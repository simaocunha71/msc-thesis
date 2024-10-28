You can use the built-in `toString()` method to convert the decimal number to binary and then slice off the first two characters. Here's how you can do it:

```javascript
const decimalToBinary = (decimal) => {
  return "db" + decimal.toString(2).slice(2) + "db";
};
```

The `toString(2)` method converts the decimal number to binary, and the `slice(2)` method removes the first two characters "db" from the result.