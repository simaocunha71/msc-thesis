To decode the string encoded with the `encodeShift` function, you need to shift each character back by 5 positions in the alphabet. Here's the corrected `decodeShift` function:

```javascript
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 + 26 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

In this function, we subtract 5 from the character code of each character, then add 26 and the character code of `"a"`, and finally take the modulus of 26. This ensures that the character code is within the range of lowercase letters. The `join("")` method is then used to concatenate the array of characters back into a single string.