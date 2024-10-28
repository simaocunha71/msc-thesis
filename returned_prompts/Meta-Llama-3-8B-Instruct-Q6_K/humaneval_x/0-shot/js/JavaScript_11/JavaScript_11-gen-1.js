```javascript
const stringXor = (a, b) => {
  if (a.length !== b.length) {
    throw new Error('Strings must be of the same length');
  }

  let result = '';

  for (let i = 0; i < a.length; i++) {
    const bitA = parseInt(a[i], 2);
    const bitB = parseInt(b[i], 2);
    const bitXor = bitA ^ bitB;
    result += bitXor.toString(2).padStart(1, '0');
  }

  return result;
};
```
Explanation:

1. First, we check if the input strings `a` and `b` have the same length. If not, we throw an error.
2. We initialize an empty string `result` to store the result of the XOR operation.
3. We iterate through each character in the input strings using a `for` loop.
4. For each character, we convert the character to its binary representation using `parseInt` with a base of 2.
5. We perform the XOR operation on the two binary values using the `^` operator.
6. We convert the result of the XOR operation back to a binary string using `toString` with a base of 2, and pad it with leading zeros if necessary using `padStart`.
7. We concatenate the resulting binary string to the `result` string.
8. Finally, we return the `result` string.

Example usage:
```javascript
console.log(stringXor('010', '110')); // Output: "100"
```