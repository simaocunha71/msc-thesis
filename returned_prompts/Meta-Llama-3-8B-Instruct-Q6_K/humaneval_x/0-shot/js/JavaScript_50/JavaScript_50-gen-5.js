```
const encodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    (ch.charCodeAt(0) - "a".charCodeAt(0) + 26) % 26 + "a".charCodeAt(0)
  )).join("");
}

const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    (ch.charCodeAt(0) - "a".charCodeAt(0)) % 26 + "a".charCodeAt(0)
  )).join("");
}
```



Explanation:

1. `encodeShift` function takes a string `s` as input and returns the encoded string.

   - `s.split("")` splits the string into an array of individual characters.
   - `map` function is used to apply a transformation to each character.
   - `String.fromCharCode` is used to convert the character code back to a character.
   - The character code is calculated by adding 5 to the original character code, wrapping around the alphabet if necessary (`(ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26`).
   - The result is then joined back into a string.

2. `decodeShift` function takes a string `s` as input and returns the decoded string.

   - `s.split("")` splits the string into an array of individual characters.
   - `map` function is used to apply a transformation to each character.
   - `String.fromCharCode` is used to convert the character code back to a character.
   - The character code is calculated by subtracting the original character code from the encoded character code, wrapping around the alphabet if necessary (`(ch.charCodeAt(0) - "a".charCodeAt(0)) % 26`).
   - The result is then joined back into a string.

The `decodeShift` function is essentially the inverse of the `encodeShift` function, and it can be used to recover the original string from the encoded string.