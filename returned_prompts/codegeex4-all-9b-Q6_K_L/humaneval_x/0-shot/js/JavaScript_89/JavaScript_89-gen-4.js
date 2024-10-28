```js
const encrypt = (s) => {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    let index = alphabet.indexOf(char);
    if (index !== -1) {
      encrypted += alphabet[(index + 4) % 26];
    } else {
      encrypted += char;
    }
  }
  return encrypted;
};
```