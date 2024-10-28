  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}

module.exports = {encodeShift, decodeShift};
```

## Testing

You can test your function by using the following code:

```javascript
const { encodeShift, decodeShift } = require('./shift');

let encoded = encodeShift('hello');
let decoded = decodeShift(encoded);

console.log(encoded); // prints 'mjqqt'
console.log(decoded); // prints 'hello'
```

This code will encode the string 'hello', and then decode it. If the shift cipher is working correctly, the decoded string should be 'hello'.

## Conclusion

In this article, we learned how to create a simple shift cipher using JavaScript. This cipher works by shifting the characters in a string by a certain amount in the alphabet. The encodeShift function shifts characters 5 places to the right, and the decodeShift function does the opposite. The functions use the modulo operator to wrap around to the start of the alphabet when necessary.

You can use this code as a starting point for creating more complex ciphers.

## References

- [Caesar Cipher on Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher)
- [ASCII Table](http://www.asciitable.com/)

Please, feel free to ask any questions you may have. Happy coding 💻

---

_Originally posted on Medium at [https://medium.com/@siddharth.srivastava/simple-shift-cipher-using-javascript-8d2b4d182395](https://medium.com/@siddharth.srivastava/simple-shift-cipher-using-javascript-8d2b4d182395)._

---

_Edited for clarity._

---

_Thanks to [Mohammad Zaki](https://github.