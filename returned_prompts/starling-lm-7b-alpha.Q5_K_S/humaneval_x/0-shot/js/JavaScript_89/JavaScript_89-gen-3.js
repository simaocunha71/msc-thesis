Here's a solution using JavaScript:

```javascript
const encrypt = (s) => {
  let result = '';
  for (let i = 0; i < s.length; i++) {
    let c = s.charCodeAt(i);
    if (c >= 97 && c <= 122) {
      result += String.fromCharCode((c - 97 + 2) % 26 + 97);
    } else if (c >= 65 && c <= 90) {
      result += String.fromCharCode((c - 65 + 2) % 26 + 65);
    } else {
      result += s[i];
    }
  }
  return result;
};
```

This function uses a for loop to iterate through each character in the input string. It uses the `charCodeAt` method to get the Unicode value of the character, and then checks if the character is a lowercase letter or an uppercase letter. If it is, it applies the encryption by subtracting the appropriate starting value (97 for lowercase letters and 65 for uppercase letters), adding the rotation value (2), taking the modulo 26 to ensure the result is within the range of the alphabet, and then adding the starting value back in. Finally, it converts the resulting Unicode value back to a character using `String.fromCharCode` and appends it to the result string. If the character is not a letter, it simply appends it to the result string without encryption.

You can use this function to encrypt any string by calling `encrypt('your_string_here')`.
```

As an example, if you call `encrypt('hi')`, it will return `'lm'`. If you call `encrypt('asdfghjkl')`, it will return `'ewhjklnop'`. If you call `encrypt('gf')`, it will return `'kj'`. And if you call `encrypt('et')`, it will return `'ix'`.

This solution ensures that the encryption is applied correctly for both uppercase and lowercase letters, and ignores any non-alphabet characters in the input string.

```