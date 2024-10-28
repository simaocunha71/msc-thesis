/*
  returns decoded string by shifting every character by -5 in the alphabet.
   */
const decodeShift  (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}

/*
  returns encoded string by shifting every character by 5 in the alphabet.
   */
const encodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

/*
  takes as input string encoded with encode_shift function. Returns decoded string.
   */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0) + 26) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

The first function, encodeShift, takes a string and returns a new string where every character in the original string is shifted 5 characters in the alphabet. The second function, decodeShift, takes an encoded string and returns the original string.

This works by converting each character to its ASCII representation (charCodeAt), then shifting it by 5, wrapping around the alphabet (using % 26) and finally converting it back to a character (String.fromCharCode).

The decodeShift function does the same, but shifts the characters back by 5 instead.

The functions return the encoded and decoded strings.

I hope this helps, and please let me know if you have any questions.















































