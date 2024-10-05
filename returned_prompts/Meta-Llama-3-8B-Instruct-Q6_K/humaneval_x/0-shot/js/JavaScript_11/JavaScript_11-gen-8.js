```javascript
const stringXor = (a, b) => {
  if (a.length !== b.length) {
    throw new Error('Strings must have the same length');
  }
  return a.split('').map((char, index) => {
    return (char === '1' && b[index] === '1') ? '0' : (char === '0' && b[index] === '0') ? '0' : '1';
  }).join('');
};
```
This function performs a binary XOR operation on two input strings. It checks if the input strings have the same length, and if not, throws an error. It then splits the strings into individual characters, maps over them, and returns the result as a string.

The mapping function checks if the characters at the current index in both strings are the same (both '1' or both '0'). If they are, it returns '0'. If they are not, it returns '1'.

Finally, it joins the resulting array of characters back into a string and returns it.