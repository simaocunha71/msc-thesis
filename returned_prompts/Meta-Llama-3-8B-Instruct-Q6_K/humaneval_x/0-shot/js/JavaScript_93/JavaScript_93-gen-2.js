Here is a JavaScript function that implements the described encoding:

```javascript
const encode = (message) => {
  return message
    .split('')
    .map((char) => {
      if (char.match(/[a-z]/i)) {
        if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
          return String.fromCharCode((char.charCodeAt(0) + 2) % 26 + 97);
        } else {
          return char.toUpperCase();
        }
      } else {
        return char;
      }
    })
    .join('');
};
```
This function works by splitting the input message into individual characters, then mapping over each character. If the character is a letter (checked using a regular expression), it checks if the character is a vowel. If it is a vowel, it shifts the character two places ahead in the alphabet (wrapping around to the start of the alphabet if necessary). If the character is not a vowel, it converts it to uppercase. Finally, it joins the modified characters back together into a string.