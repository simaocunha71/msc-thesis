```js
const encode = (message) => {
  let newMsg = '';
  for (let i = 0; i < message.length; i++) {
    let c = message[i];
    if (c.match(/[a-z]/)) {
      if (c.match(/[aeiou]/)) {
        c = String.fromCharCode(c.charCodeAt(0) + 2);
      } else {
        c = c.toUpperCase();
      }
    } else if (c.match(/[A-Z]/)) {
      if (c.match(/[AEIOU]/)) {
        c = String.fromCharCode(c.charCodeAt(0) + 2);
      } else {
        c = c.toLowerCase();
      }
    }
    newMsg += c;
  }
  return newMsg;
}
```
