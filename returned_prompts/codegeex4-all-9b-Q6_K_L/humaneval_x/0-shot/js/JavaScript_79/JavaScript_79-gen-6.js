The function can be created as follows:

```javascript
const decimalToBinary = (decimal) => {
  return `db${decimal.toString(2)}db`;
}
```

This function uses the built-in `toString()` method of JavaScript numbers to convert the given decimal number to its binary representation. The `toString(2)` method takes an argument of 2, which specifies that the conversion should be done to base-2 (binary). The resulting binary string is then wrapped with the "db" strings at the beginning and end, and returned as the final result.