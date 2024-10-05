Here is a JavaScript function that implements the described encryption algorithm:

```javascript
const encrypt = (s) => {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const encrypted = [];
  for (let char of s.toLowerCase()) {
    if (char === ' ') {
      encrypted.push(' ');
    } else {
      const index = alphabet.indexOf(char);
      const newIndex = (index + 2 * 2) % alphabet.length;
      encrypted.push(alphabet[newIndex]);
    }
  }
  return encrypted.join('');
};
```

This function works by iterating over each character in the input string. If the character is a space, it is added to the encrypted string as is. If the character is a letter, its index in the alphabet is found, and then the index is incremented by 2 multiplied by 2, wrapping around to the beginning of the alphabet if necessary. The resulting character is then added to the encrypted string. Finally, the encrypted string is returned.

You can test this function with the examples you provided:

```javascript
console.log(encrypt('hi')); // Output: "lm"
console.log(encrypt('asdfghjkl')); // Output: "ewhjklnop"
console.log(encrypt('gf')); // Output: "kj"
console.log(encrypt('et')); // Output: "ix"
```



This function assumes that the input string only contains letters and spaces. If the input string may contain other characters, you may want to add error checking to handle these cases.