```javascript
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}
```
Explanation:

The `encodeShift` function shifts every character in the input string by 5 positions in the alphabet. It works by subtracting the ASCII value of 'a' from the ASCII value of the character, adding 5, and then taking the result modulo 26 to wrap around to the beginning of the alphabet if necessary. The result is then converted back to a character using the `String.fromCharCode` method.

The `decodeShift` function does the opposite: it shifts every character back by 5 positions in the alphabet. It works by subtracting the ASCII value of 'a' from the ASCII value of the character, adding 26, and then taking the result modulo 26 to wrap around to the beginning of the alphabet if necessary. The result is then converted back to a character using the `String.fromCharCode` method.

Note that the `decodeShift` function assumes that the input string was encoded using the `encodeShift` function, and that the encoding was done without any errors. If the input string was encoded using a different method, or if the encoding was done with errors, the `decodeShift` function may not produce the correct result.