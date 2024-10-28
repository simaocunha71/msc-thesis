```js
const encode = (message) => {
  let msg = '';
  for (let i = 0; i < message.length; i++) {
    let c = message[i];
    if (c.match(/[a-z]/)) {
      c = c.toUpperCase().charCodeAt(0) - 97;
      if (c == 0 || c == 4 || c == 8 || c == 14 || c == 20) {
        c = String.fromCharCode(c + 2 + 65);
      } else {
        c = String.fromCharCode(c + 65);
      }
      if (i % 2 == 0) {
        c = c.toUpperCase();
      } else {
        c = c.toLowerCase();
      }
    }
    msg += c;
  }
  return msg;
}
```