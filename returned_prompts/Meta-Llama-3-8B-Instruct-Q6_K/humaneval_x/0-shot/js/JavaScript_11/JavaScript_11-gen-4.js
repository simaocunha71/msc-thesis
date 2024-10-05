```
const stringXor = (a, b) => {
  const maxLen = Math.max(a.length, b.length);
  let result = '';
  for (let i = 0; i < maxLen; i++) {
    const ai = a[i] === undefined ? '0' : a[i];
    const bi = b[i] === undefined ? '0' : b[i];
    result += (ai === bi) ? '0' : '1';
  }
  return result;
};
```


Explanation:

1. We first find the maximum length of the two input strings `a` and `b`. This is done using the `Math.max` function.
2. We initialize an empty string `result` that will store the result of the binary XOR operation.
3. We loop through each character in the strings, up to the maximum length. If a character is not present in one of the strings, we use the default value '0'.
4. For each pair of characters, we perform the binary XOR operation. If the characters are the same, the result is '0', otherwise it's '1'.
5. We concatenate the result of each XOR operation to the `result` string.
6. Finally, we return the `result` string.

For example, if we call `stringXor('010', '110')`, the function will return '100', which is the result of performing the binary XOR operation on the two input strings.