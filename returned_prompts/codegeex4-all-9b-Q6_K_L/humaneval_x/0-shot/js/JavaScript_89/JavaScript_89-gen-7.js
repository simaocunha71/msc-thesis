```javascript
const encrypt = (s) => {
  let alphabet = 'abcdefghijklmnopqrstuvwxyz';
  let encrypted = '';
  for (let i = 0; i < s.length; i++) {
    let index = alphabet.indexOf(s[i].toLowerCase());
    if (index === -1) {
      encrypted += s[i];
    } else {
      encrypted += alphabet[(index + 4) % 26];
    }
  }
  return encrypted;
}
```

This function uses a for loop to iterate through each character in the input string. It checks if the character is a letter and then finds its index in the alphabet. If the character is not a letter, it is added to the encrypted string as is. If the character is a letter, it is shifted down by two multiplied to two places in the alphabet and added to the encrypted string. The encrypted string is returned at the end of the function.