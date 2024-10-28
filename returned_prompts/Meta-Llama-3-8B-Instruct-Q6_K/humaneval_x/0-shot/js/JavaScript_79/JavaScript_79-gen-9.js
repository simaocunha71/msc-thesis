Here is a JavaScript function that converts a decimal number to binary format:

```javascript
const decimalToBinary = (decimal) => {
  let binary = decimal.toString(2);
  return 'db' + binary + 'db';
};
```

In this function, we use the `toString()` method with the base 2 argument to convert the decimal number to a binary string. Then we add the extra 'db' characters to the beginning and end of the binary string.

For example, if we call `decimalToBinary(15)`, the function will return the string "db1111db". If we call `decimalToBinary(32)`, the function will return the string "db100000db". This is the expected output based on the problem description.