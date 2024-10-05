```js
const allPrefixes = (string) => {
  let res = [];
  for (let i = 0; i < string.length; i++) {
    res.push(string.slice(0, i + 1));
  }
  return res;
}
```
