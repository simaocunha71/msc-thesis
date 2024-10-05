```javascript
const stringXor = (a, b) => {
  let result = '';
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    const bitA = a[i] || '0';
    const bitB = b[i] || '0';
    result += (bitA === '1' && bitB === '1') ? '0' : (bitA === '0' && bitB === '0') ? '0' : '1';
  }
  return result;
};
```
Explanation:
The function `stringXor` takes two binary strings `a` and `b` as input. It iterates through the longer of the two strings, and for each position, it checks the bits of `a` and `b`. If both bits are 1, the result bit is 0. If both bits are 0, the result bit is also 0. If the bits are different (one 0 and one 1), the result bit is 1. The result is built as a string by concatenating the result bits.

The `|| '0'` is used to ensure that the iteration goes through all positions of the longer string. If a position in the shorter string is reached, the corresponding bit from the longer string is used.

The function returns the resulting binary string. For example, `stringXor('010', '110')` returns '100'.