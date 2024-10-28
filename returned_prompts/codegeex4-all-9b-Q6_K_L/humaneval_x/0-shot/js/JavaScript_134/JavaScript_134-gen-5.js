```js
const checkIfLastCharIsALetter = (txt) => {
  if(txt.length === 0) return false;
  const lastChar = txt[txt.length - 1];
  if(!/[a-zA-Z]/.test(lastChar)) return false;
  const lastWord = txt.split(' ').slice(-1)[0];
  return lastWord.length === txt.length;
}
```
