You can use the built-in JavaScript function `toString()` with the radix argument set to 2 to convert a decimal number to binary. Here's how you can implement the `decimalToBinary` function:

```javascript
const decimalToBinary = (decimal) => {
  return `db${decimal.toString(2)}db`;
}
```

This function takes a decimal number as input and returns a string in binary format with the extra characters 'db' at the beginning and at the end.