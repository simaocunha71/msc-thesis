Here is the solution in JavaScript:

```javascript
const decimalToBinary = (decimal) => {
  let binary = decimal.toString(2);
  return `db${binary}db`;
};

console.log(decimalToBinary(15));  // returns "db1111db"
console.log(decimalToBinary(32));  // returns "db100000db"
```

This solution converts the decimal number to binary using JavaScript's built-in `toString` method. The `toString` method takes a radix (base) as an argument, and in this case, we use 2 to convert to binary. The resulting binary number is then wrapped with the `db` characters at the beginning and end of the string.