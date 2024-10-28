```js
const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt.trim().slice(-1);
  return /^[a-zA-Z]$/.test(lastChar) && !/\w/.test(txt.slice(-2));
}
```
