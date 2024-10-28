Here is the solution:

```javascript
const decimalToBinary = (decimal) => {
  return 'db' + decimal.toString(2) + 'db';
};
```
Explanation:
The `toString(2)` method is used to convert the decimal number to a binary string. The `toString()` method converts a number to a string, and the second argument `2` specifies the base (in this case, binary). The `db` characters are concatenated at the beginning and end of the binary string to meet the format requirement. The function returns the resulting string.