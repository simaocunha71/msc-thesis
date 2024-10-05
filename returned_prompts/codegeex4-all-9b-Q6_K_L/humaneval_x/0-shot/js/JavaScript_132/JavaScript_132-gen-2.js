```js
const isNested = (string) => {
  let open = 0;
  let close = 0;
  for (let i = 0; i < string.length; i++) {
    if (string[i] === '[') {
      open++;
    } else if (string[i] === ']') {
      close++;
    }
    if (close > open) {
      return true;
    }
  }
  return false;
}
```
