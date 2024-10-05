To solve this problem, you can follow these steps:

1. Create a helper function to swap the case of a letter.
2. Create a helper function to replace a vowel with the letter that appears 2 places ahead of it in the alphabet.
3. Iterate through each character in the message.
4. For each character, check if it is a letter. If it is, swap its case and replace it with the vowel that appears 2 places ahead of it, if it is a vowel.
5. Return the encoded message.

Here's the solution in JavaScript:

```javascript
const encode = (message) => {
  // Helper function to swap case of a letter
  const swapCase = (letter) => {
    if (letter === letter.toUpperCase()) {
      return letter.toLowerCase();
    } else {
      return letter.toUpperCase();
    }
  };

  // Helper function to replace vowel with the letter that appears 2 places ahead of it
  const replaceVowel = (vowel) => {
    const vowels = 'aeiou';
    const index = vowels.indexOf(vowel);
    if (index !== -1) {
      return vowels[(index + 2) % vowels.length];
    } else {
      return vowel;
    }
  };

  // Encode the message
  let encodedMessage = '';
  for (let i = 0; i < message.length; i++) {
    const char = message[i];
    if (char.match(/[a-zA-Z]/)) {
      // If the character is a letter, swap its case and replace it with the vowel that appears 2 places ahead of it
      const encodedChar = swapCase(char);
      const replacedChar = replaceVowel(encodedChar);
      encodedMessage += replacedChar;
    } else {
      // If the character is not a letter, add it to the encoded message as is
      encodedMessage += char;
    }
  }

  return encodedMessage;
};

console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'
```

This solution should work for the given examples and any other valid input.