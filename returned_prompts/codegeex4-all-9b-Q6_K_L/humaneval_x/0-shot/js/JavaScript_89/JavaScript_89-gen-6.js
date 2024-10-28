Here's one way you can solve this problem:

```javascript
const encrypt = (s) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const shiftedAlphabet = alphabet.slice(4).concat(alphabet.slice(0, 4));
  let encryptedString = '';
  
  for (let i = 0; i < s.length; i++) {
    const charIndex = alphabet.indexOf(s[i]);
    
    if (charIndex !== -1) {
      encryptedString += shiftedAlphabet[charIndex];
    } else {
      encryptedString += s[i];
    }
  }
  
  return encryptedString;
}
```

This function works by first defining the alphabet and the shifted alphabet where each letter is two places to the right of the original position. Then it goes through each character in the input string and checks if it exists in the original alphabet. If it does, it replaces the character with the corresponding character in the shifted alphabet. If the character doesn't exist in the alphabet, it leaves it as is. Finally, it returns the encrypted string.