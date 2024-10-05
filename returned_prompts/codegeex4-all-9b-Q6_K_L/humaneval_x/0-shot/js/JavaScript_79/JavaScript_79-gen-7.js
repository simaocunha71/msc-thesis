You can use the built-in method `toString(2)` to convert a number to its binary representation. Then, you can prepend and append 'db' to the result string. Here's a possible solution:

```javascript
const decimalToBinary = (decimal) => {
  return `db${decimal.toString(2)}db`;
}
```

This will return the binary representation of the given decimal number, with 'db' at the beginning and end of the string.