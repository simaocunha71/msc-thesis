Here is the solution:
```
const decimalToBinary = (decimal) => {
  return 'db' + (decimal.toString(2)).padStart(8, '0') + 'db';
};
```
Explanation:

* `decimal.toString(2)` converts the decimal number to a binary string.
* `padStart(8, '0')` ensures that the binary string is always 8 characters long by padding it with leading zeros if necessary.
* `'db'` is added at the beginning and end of the string to match the desired format.

For example, `decimalToBinary(15)` returns `'db1111db'` and `decimalToBinary(32)` returns `'db100000db'`.