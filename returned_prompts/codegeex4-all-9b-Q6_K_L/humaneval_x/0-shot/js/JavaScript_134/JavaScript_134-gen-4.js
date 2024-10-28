```js
const checkIfLastCharIsALetter = (txt) => {
  return /^[a-zA-Z]$/.test(txt.trim().slice(-1));
}
```