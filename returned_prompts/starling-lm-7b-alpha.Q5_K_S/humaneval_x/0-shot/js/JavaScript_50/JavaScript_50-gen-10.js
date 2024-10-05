
Your `decodeShift` function is almost correct, but you have an unnecessary `"a".charCodeAt(0)` in the calculation. You can correct your `decodeShift` function by removing the `"a".charCodeAt(0)`. Here is the corrected `decodeShift` function:

```javascript
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5) % 26)
  )).join("");
}
```

This should correctly reverse the `encodeShift` function.

Explanation:

In the `decodeShift` function, you are trying to reverse the `encodeShift` function, which shifts every character in the string by 5 in the alphabet.