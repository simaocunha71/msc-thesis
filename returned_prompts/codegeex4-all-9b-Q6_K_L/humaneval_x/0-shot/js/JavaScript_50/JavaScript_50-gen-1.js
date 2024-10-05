You can solve this problem by using the ASCII values of the characters in the string and subtracting 5 from them. Here's the solution:

```javascript
function decodeShift(s) {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 + 26 - "a".charCodeAt(0)) % 26) + "a".charCodeAt(0)
  )).join("");
}
```

In this solution, we first split the string into an array of characters using the `split("")` method. Then, we map over each character and use the `charCodeAt(0)` method to get the ASCII value of the character. We subtract 5 from the ASCII value and add 26 to ensure that the result is always a positive number between 0 and 25. Finally, we use the `String.fromCharCode()` method to convert the ASCII value back to a character and join the array of characters back into a string using the `join("")` method.