```javascript
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

Explanation:
The `decodeShift` function is the inverse of the `encodeShift` function. It takes an encoded string as input and returns the original string by shifting every character back by 5 in the alphabet.

The function works by iterating over each character in the input string using `map`. For each character, it calculates the ASCII code of the character 5 positions before it in the alphabet using the formula `(ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26`. This is done by subtracting the ASCII code of 'a' from the character's ASCII code, adding 26 to wrap around the alphabet if necessary, and then taking the remainder when divided by 26 to ensure the result is within the range of 'a' to 'z'.

The resulting ASCII code is then converted back to a character using `String.fromCharCode`, and the resulting characters are joined together to form the decoded string using `join`.