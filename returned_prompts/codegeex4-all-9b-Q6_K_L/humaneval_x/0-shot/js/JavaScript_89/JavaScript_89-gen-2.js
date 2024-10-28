```javascript
const encrypt = (s) => {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let index = alphabet.indexOf(s[i].toLowerCase());
    if (index !== -1) {
      let newIndex = (index + 4 * 2) % 26;
      encrypted += alphabet[newIndex];
    } else {
      encrypted += s[i];
    }
  }
  return encrypted;
}
```