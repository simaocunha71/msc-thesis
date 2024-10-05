```
const stringXor = (a, b) => {
  return (a.split('').map((c, i) => (c === b[i] ? '0' : '1')).join(''));
};
```


Explanation:
The function `stringXor` takes two binary strings `a` and `b` as input. It then uses the `map` method to iterate over each character in the strings, comparing them character by character. If the characters are the same, it returns '0', otherwise it returns '1'. The result is then joined back into a string using the `join` method. This effectively performs a binary XOR operation on the two input strings.