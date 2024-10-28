```js
const stringXor = (a, b) => {
  let maxLen = Math.max(a.length, b.length);
  a = a.padStart(maxLen, '0');
  b = b.padStart(maxLen, '0');
  let result = '';
  for (let i = 0; i < maxLen; i++) {
    if (a[i] === b[i]) {
      result += '0';
    } else {
      result += '1';
    }
  }
  return result;
}
```
