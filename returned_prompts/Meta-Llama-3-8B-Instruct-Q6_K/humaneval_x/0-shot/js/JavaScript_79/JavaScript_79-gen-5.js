Here is a JavaScript solution for the problem:

```javascript
const decimalToBinary = (decimal) => {
  return 'db' + decimal.toString(2) + 'db';
}
```
This function uses the built-in `toString()` method in JavaScript, which converts the given number to a string. The second argument to `toString()` is the base of the number system. In this case, we pass 2 to convert the number to binary.

The function first prepends 'db' to the result and then appends 'db' to the end. This is in accordance with the problem statement, which requires the extra 'db' characters at the beginning and end of the string.

For example, if you call `decimalToBinary(15)`, the function will return the string 'db1111db'. Similarly, `decimalToBinary(32)` will return 'db100000db'.