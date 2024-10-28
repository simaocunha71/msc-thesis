```javascript
const encrypt = (s) => {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let index = alphabet.indexOf(s[i]);
    if (index === -1) {
      encrypted += s[i];
    } else {
      let newIndex = (index + 4) % 26;
      encrypted += alphabet[newIndex];
    }
  }
  return encrypted;
}
```
