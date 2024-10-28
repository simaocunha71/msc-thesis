You can solve this problem by using the built-in JavaScript method `toString()`. This method converts a number to a string representation of the number in the specified base. In this case, the base is 2 for binary.

Here's how you can do it:

```javascript
const decimalToBinary = (decimal) => {
  return 'db' + decimal.toString(2) + 'db';
};
```

The `toString(2)` method converts the decimal number to its binary representation. The `+` operator is used to concatenate the 'db' characters at the beginning and end of the string.

Let's test the function with the given examples:

```javascript
console.log(decimalToBinary(15));   // Output: "db1111db"
console.log(decimalToBinary(32));   // Output: "db100000db"
```

The function works as expected!