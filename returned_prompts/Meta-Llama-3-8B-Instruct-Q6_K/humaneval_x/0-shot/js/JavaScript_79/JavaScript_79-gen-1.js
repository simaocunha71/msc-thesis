```
const decimalToBinary = (decimal) => {
  return 'db' + decimal.toString(2) + 'db';
};
```
Explanation:
The function takes a decimal number as input and converts it to a binary string using the `toString(2)` method, which converts a number to a string in the given base. The base 2 corresponds to binary. The 'db' characters are added at the beginning and end of the string to match the required format. The function returns the resulting string.