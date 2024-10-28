Here is a function in JavaScript that accomplishes the task:

```javascript
const encode = (message) => {
  return message.replace(/([a-z])/g, (match, char) => {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
      let newChar = String.fromCharCode(char.charCodeAt(0) + 2);
      if (newChar.charCodeAt(0) > 'z'.charCodeAt(0)) {
        newChar = String.fromCharCode('a'.charCodeAt(0) + (newChar.charCodeAt(0) - 'z'.charCodeAt(0) - 1));
      }
      return newChar.toUpperCase();
    } else {
      return char.toUpperCase();
    }
  }).replace(/([A-Z])/g, (match, char) => {
    if (char === 'A' || char === 'E' || char === 'I' || char === 'O' || char === 'U') {
      let newChar = String.fromCharCode(char.charCodeAt(0) - 2);
      if (newChar.charCodeAt(0) < 'A'.charCodeAt(0)) {
        newChar = String.fromCharCode('Z'.charCodeAt(0) - (char.charCodeAt(0) - 'A'.charCodeAt(0) + 1));
      }
      return newChar.toLowerCase();
    } else {
      return char.toLowerCase();
    }
  });
};
```

This function uses a regular expression to iterate over each character in the message. If the character is a vowel (both lowercase and uppercase), it is replaced with the character that is two places ahead of it in the alphabet. If the character is not a vowel, it is simply converted to uppercase. The function then repeats this process for lowercase letters, converting them to lowercase. The result is a message that has been encoded according to the problem's specifications. 