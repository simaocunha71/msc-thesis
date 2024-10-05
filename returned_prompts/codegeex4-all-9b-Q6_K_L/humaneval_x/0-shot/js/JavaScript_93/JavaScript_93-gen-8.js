```js
const encode = (message) => {
  const vowels = 'aeiouAEIOU';
  return message.split('').map(char => {
    if (vowels.includes(char)) {
      return String.fromCharCode(char.charCodeAt(0) + 2);
    } else if (char === char.toUpperCase()) {
      return char.toLowerCase();
    } else {
      return char.toUpperCase();
    }
  }).join('');
}
```