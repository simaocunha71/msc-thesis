Here's a JavaScript function to encode and decode a string using a Caesar cipher with a shift of 5:

```javascript
const encodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) + 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

You can use these functions as follows:

```javascript
const originalString = "hello";
const encodedString = encodeShift(originalString);
console.log(encodedString); // outputs "mjqqt"

const decodedString = decodeShift(encodedString);
console.log(decodedString); // outputs "hello"
```

In the `encodeShift` function, we iterate over each character in the input string, calculate the ASCII code for the encoded character, and then join the encoded characters back into a string.

In the `decodeShift` function, we do the opposite: we iterate over each character in the input string, calculate the ASCII code for the decoded character, and then join the decoded characters back into a string.

Note that these functions assume that the input string only contains lowercase letters. If the input string can contain uppercase letters, digits, or special characters, you would need to modify the functions accordingly. Also, these functions do not handle non-ASCII characters. If you need to handle non-ASCII characters, you would need to use a more sophisticated approach.