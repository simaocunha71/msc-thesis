```js
const stringXor = (a, b) => {
  let res = '';
  for (let i = 0; i < a.length; i++) {
    res += a[i] ^ b[i];
  }
  return res;
}
```
