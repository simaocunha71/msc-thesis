The task is to write a JavaScript function that decodes a string that has been encoded using a Caesar cipher with a shift of 5. The Caesar cipher is a type of substitution cipher in which each character in the plaintext is 'shifted' a certain number of places down or up the alphabet. In this case, each letter is shifted 5 places down the alphabet.

Here's the JavaScript function that decodes the string:

```javascript
const decodeShift = (s) => {
  return s.split("")
    .map(ch => String.fromCharCode(
      ((ch.charCodeAt(0) - 5 + 26 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
    ))
    .join("");
}
```

This function works similarly to the `encodeShift` function, but instead of adding 5 to the character code, it subtracts 5. The addition of 26 ensures that the character code is within the range of the alphabet. The modulo operator `%` is used to wrap around the alphabet if the character code goes below 'a' or above 'z'. The `join("")` method is used to combine the characters back into a string.

To use this function, you can call it with an encoded string as the argument, like this:

```javascript
const encodedString = encodeShift("hello");
const decodedString = decodeShift(encodedString);
console.log(decodedString); // Output: "hello"
```

In this example, the `encodeShift` function is used to encode the string "hello", and the `decodeShift` function is used to decode the encoded string back to "hello".