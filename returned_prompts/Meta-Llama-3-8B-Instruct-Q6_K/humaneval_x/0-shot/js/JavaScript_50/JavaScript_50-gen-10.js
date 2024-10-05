```
const encodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    (ch.charCodeAt(0) - "a".charCodeAt(0) + 5) % 26 + "a".charCodeAt(0)
  )).join("");
}

const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    (ch.charCodeAt(0) - "a".charCodeAt(0) - 5) % 26 + "a".charCodeAt(0)
  )).join("");
}
```
The encodeShift function shifts every character in the input string by 5 positions in the alphabet. It does this by subtracting the ASCII value of 'a' from the ASCII value of the character, adding 5, taking the remainder when divided by 26 (the number of letters in the alphabet), and then adding back the ASCII value of 'a'. This ensures that the output is also a string of lowercase letters.

The decodeShift function is the inverse of the encodeShift function. It shifts every character in the input string by -5 positions in the alphabet, effectively reversing the encoding process. The calculation is similar to the one in the encodeShift function, but with a minus sign instead of a plus sign. This ensures that the output is the original input string.