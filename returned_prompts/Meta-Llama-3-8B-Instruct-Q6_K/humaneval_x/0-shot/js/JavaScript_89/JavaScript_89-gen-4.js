Here is a simple solution in JavaScript:
```javascript
const encrypt = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let char = s[i];
    if (char.match(/[a-z]/i)) {
      let ascii = char.charCodeAt(0);
      if (char === char.toUpperCase()) {
        ascii -= 65; // ASCII value for 'A'
      } else {
        ascii -= 97; // ASCII value for 'a'
      }
      ascii = (ascii + 2 * 2) % 26;
      if (char === char.toUpperCase()) {
        result += String.fromCharCode(ascii + 65);
      } else {
        result += String.fromCharCode(ascii + 97);
      }
    } else {
      result += char;
    }
  }
  return result;
};
```
Here's a breakdown of how the function works:

1. We iterate through each character `char` in the input string `s`.
2. We check if the character is a lowercase or uppercase letter using a regular expression. If it's not a letter, we simply append it to the result string as is.
3. If it is a letter, we convert it to its ASCII code using the `charCodeAt` method.
4. We subtract the ASCII value of 'A' or 'a' depending on whether the letter is uppercase or lowercase, respectively.
5. We add 2 multiplied by 2 to the resulting ASCII value, which effectively shifts the letter down by 4 places in the alphabet.
6. We take the result modulo 26 to ensure we wrap around the alphabet if necessary.
7. We convert the resulting ASCII value back to a character using the `String.fromCharCode` method, and append it to the result string.
8. Finally, we return the encrypted result string.

You can test the function with the examples you provided to see that it produces the expected output. Let me know if you have any questions or need further clarification! 😊

Example usage:
```javascript
console.log(encrypt('hi')); // Output: 'lm'
console.log(encrypt('asdfghjkl')); // Output: 'ewhjklnop'
console.log(encrypt('gf')); // Output: 'kj'
console.log(encrypt('et')); // Output: 'ix'
```