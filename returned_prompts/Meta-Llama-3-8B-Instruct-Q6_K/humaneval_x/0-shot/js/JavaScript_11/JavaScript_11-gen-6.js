The XOR operation is applied by iterating over the strings and performing a binary XOR operation on corresponding bits. The result is then converted back to a string.

Here is the solution in JavaScript:

```javascript
const stringXor = (a, b) => {
  if (a.length !== b.length) {
    throw new Error('Strings must be of the same length');
  }
  return a.split('').map((x, i) => (x ^ b[i])).join('');
};
```
In this solution, we first check if the lengths of the input strings are equal. If they are not, we throw an error. Then, we use the `split` method to split the strings into arrays of characters, and the `map` method to apply the XOR operation to corresponding elements of the arrays. The `join` method is used to convert the resulting array back to a string. The XOR operation is performed using the `^` operator in JavaScript, which performs a bitwise XOR operation on the operands. The result is a string consisting of the binary XOR of the input strings.