```javascript
const encrypt = (s) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let index = alphabet.indexOf(s[i].toLowerCase());
    if (index !== -1) {
      let newIndex = (index + 4) % 26;
      encrypted += alphabet[newIndex];
    } else {
      encrypted += s[i];
    }
  }
  return encrypted;
}
```