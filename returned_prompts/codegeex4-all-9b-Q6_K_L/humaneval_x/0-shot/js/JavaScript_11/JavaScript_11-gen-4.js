```js
const stringXor = (a, b) => {
  // check if strings are of equal length
  if (a.length !== b.length) {
    throw new Error('Strings must be of equal length');
  }
  // perform XOR on each pair of characters and join to form result
  return [...a].map((c, i) => c ^ b[i]).join('');
}
```
