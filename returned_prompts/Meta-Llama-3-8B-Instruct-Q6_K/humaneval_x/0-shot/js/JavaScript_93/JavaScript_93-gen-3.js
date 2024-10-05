Here is the solution in JavaScript:

```javascript
const encode = (message) => {
  let result = '';
  for (let i = 0; i < message.length; i++) {
    let char = message[i];
    if (char.match(/[a-z]/i)) {
      if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
        result += String.fromCharCode((char.charCodeAt(0) + 2) % 26 + 97);
      } else {
        result += char.toUpperCase();
      }
    } else {
      result += char;
    }
  }
  return result;
};
```
This function iterates over each character in the message. If the character is a letter (checked using the `match` method with a regular expression), it checks if it's a vowel (checked by comparing the character to the strings 'a', 'e', 'i', 'o', and 'u'). If it's a vowel, it replaces it with the letter that appears 2 places ahead of it in the alphabet (using the `charCodeAt` method to get the ASCII code of the character, adding 2, taking the modulus of 26 to wrap around the alphabet, and converting the result back to a character using the `String.fromCharCode` method). If it's not a vowel, it converts it to uppercase using the `toUpperCase` method. If the character is not a letter (e.g. it's a space or punctuation mark), it leaves it unchanged. The result is the encoded message.