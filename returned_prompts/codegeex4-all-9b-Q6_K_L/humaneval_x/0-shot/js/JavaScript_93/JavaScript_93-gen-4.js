```js
const encode = (message) => {
  return message.split('').map(char => {
    if (char.match(/[A-Za-z]/)) {
      let lower = char.toLowerCase();
      if (lower.match(/[aeiou]/)) {
        return String.fromCharCode(lower.charCodeAt(0) + 2);
      } else {
        return lower === char ? char.toUpperCase() : char.toLowerCase();
      }
    } else {
      return char;
    }
  }).join('');
}
```
