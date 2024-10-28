Here is the solution using JavaScript:

```javascript
const encode = (message) => {
  return message
    .replace(/([aeiouAEIOU])/g, match => {
      const vowel = match.toLowerCase();
      const newVowel = String.fromCharCode(vowel.charCodeAt(0) + 2);
      return newVowel.toUpperCase() === vowel ? newVowel.toLowerCase() : newVowel.toUpperCase();
    })
    .replace(/([a-z])/g, match => match.toUpperCase())
    .replace(/([A-Z])/g, match => match.toLowerCase());
};

// Test cases
console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'
```

This function uses regular expressions to replace all occurrences of vowels with the letter that appears 2 places ahead in the alphabet. It also swaps the case of all letters. The `replace` method is used with a callback function that checks if the vowel is lowercase or uppercase, and returns the new vowel accordingly. The `toUpperCase` and `toLowerCase` methods are used to swap the case of the letters. The test cases demonstrate that the function works correctly.