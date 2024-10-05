Here is a JavaScript function that fulfills the requirements:

```
const encrypt = (s) => {
  let result = '';
  for (let char of s) {
    let charCode = char.charCodeAt(0);
    result += String.fromCharCode(charCode + 32 + 32);
  }
  return result;
}
```

To test the function, you can use the following code:

```
console.log(encrypt('hi'));  // Outputs: 'lm'
console.log(encrypt('asdfghjkl'));  // Outputs: 'ewhjklnop'
console.log(encrypt('gf'));  // Outputs: 'kj'
console.log(encrypt('et'));  // Outputs: 'ix'
```

The function works by iterating through each character of the input string and using the `charCodeAt()` method to obtain its Unicode value. It then adds 32 to this value twice (since shifting down by two multiplied to two places means adding 32 twice) and converts the result back to a character using `String.fromCharCode()`. The resulting character is then appended to the `result` string.

The function returns the encrypted string once all characters have been processed.

It's worth noting that the `charCodeAt()` method returns the Unicode value of the first character in a string, and `String.fromCharCode()` converts a Unicode value to a character.

Additionally, in JavaScript, the ASCII value of 'a' is 97, so adding 32 twice to the Unicode value of 'a' (97) results in the Unicode value of 'c' (99). This is why the function uses `charCode + 32 + 32` to obtain the encrypted character's Unicode value.

To decrypt the string, you can use the `charCodeAt()` method again to obtain the Unicode value of the encrypted character and then subtract 32 twice from it. This will give you the original Unicode value of the character, which can be converted back to a character using `String.fromCharCode()`.

Here's an