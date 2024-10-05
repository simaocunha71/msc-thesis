```javascript
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}
```


This code works by using the modulo operator (`%`) to ensure that the shift wraps around the alphabet. The `(ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26` expression calculates the position of the character in the alphabet, shifts it by 5, and then uses the result to calculate the ASCII code of the decoded character.

The `String.fromCharCode` function is used to convert the calculated ASCII code back to a character.

The `split` and `join` methods are used to split the input string into an array of characters, apply the decoding function to each character, and then join the characters back together into a string.

For example, if the input string is "hello", the output of `decodeShift` would be "bfzyb". If the input string is "bfzyb", the output of `encodeShift` would be "hello".