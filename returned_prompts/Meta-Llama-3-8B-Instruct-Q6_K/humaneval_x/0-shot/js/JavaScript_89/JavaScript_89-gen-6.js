```javascript
const alphabet = 'abcdefghijklmnopqrstuvwxyz';
const shift = 4; // 2 * 2

const encrypted = s.split('').map((char) => {
  if (!char.match(/[a-z]/)) return char; // if not a letter, leave it as it is

  const index = alphabet.indexOf(char.toLowerCase());
  if (index === -1) return char; // if char is not in the alphabet, leave it as it is

  const newIndex = (index + shift) % alphabet.length;
  return alphabet[newIndex];
}).join('');

return encrypted;
```
This function first splits the string into individual characters. It then maps over each character, checking if it's a letter (ignoring non-letter characters). If it is a letter, it finds its index in the alphabet, calculates the new index by adding the shift (4 in this case), and returns the character at the new index. If the character is not in the alphabet, it leaves it as it is. Finally, it joins the encrypted characters back into a string and returns it.