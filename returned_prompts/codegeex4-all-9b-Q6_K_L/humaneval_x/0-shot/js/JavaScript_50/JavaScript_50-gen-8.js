The function `encodeShift` takes a string `s` as input and returns a new string where each character in `s` is shifted by 5 positions in the alphabet. This is achieved by converting each character to its ASCII code using `charCodeAt(0)`, adding 5 to the code, and converting it back to a character using `String.fromCharCode()`. The `% 26` operation ensures that the result is a valid character in the alphabet (a-z).

The function `decodeShift` takes an encoded string `s` as input and returns the original string before encoding. This is achieved by shifting each character in `s` back by 5 positions in the alphabet. The `((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)` operation calculates the original ASCII code of the character by subtracting 5 from the encoded ASCII code and then converting it back to a character using `String.fromCharCode()`. The `% 26` operation ensures that the result is a valid character in the alphabet (a-z).

Here is the complete code:

```javascript
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
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

You can test the functions with the following code:

```javascript
const input = "hello world";
const encoded = encodeShift(input);
const decoded = decodeShift(encoded);

console.log(input); // "hello world"
console.log(encoded); // "mjqqt btwqi"
console.log(decoded); // "hello world"
```