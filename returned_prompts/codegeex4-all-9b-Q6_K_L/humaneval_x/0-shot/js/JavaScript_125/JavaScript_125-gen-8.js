```js
const splitWords = (txt) => {
  if (txt.includes(' ')) {
    return txt.split(' ');
  }
  if (txt.includes(',')) {
    return txt.split(',');
  }
  let count = 0;
  for (let i = 0; i < txt.length; i++) {
    if (txt[i] === txt[i].toLowerCase() && (txt[i].charCodeAt(0) - 'a'.charCodeAt(0)) % 2 !== 0) {
      count++;
    }
  }
  return count;
}
```
