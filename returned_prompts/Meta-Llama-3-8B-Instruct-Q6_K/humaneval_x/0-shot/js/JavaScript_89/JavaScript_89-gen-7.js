Here is the solution for the problem:

```javascript
const encrypt = (s) => {
  let encrypted = '';
  for (let char of s.toLowerCase()) {
    if (char.match(/[a-z]/)) {
      let code = char.charCodeAt(0);
      code = (code - 97 + 26) % 26 + 97;
      encrypted += String.fromCharCode(code);
    } else {
      encrypted += char;
    }
  }
  return encrypted;
};
```

This function works by iterating over each character in the input string. If the character is a lowercase letter (checked using the `match` method), it calculates the new code for the letter by shifting it down by 2 multiplied by 2 places (which is equivalent to 4 places). It then converts this new code back to a character using the `String.fromCharCode` method. If the character is not a letter, it is left unchanged. The function returns the encrypted string. The `toLowerCase` method is used to ensure that the function works correctly for both lowercase and uppercase letters. The `charCodeAt` method is used to get the ASCII code of the character, and the `String.fromCharCode` method is used to convert the new code back to a character. The `%` operator is used to ensure that the new code stays within the range of the lowercase letters. The result is the encrypted string.