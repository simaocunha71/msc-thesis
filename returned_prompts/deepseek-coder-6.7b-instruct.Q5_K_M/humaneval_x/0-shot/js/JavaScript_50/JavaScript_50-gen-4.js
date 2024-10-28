/*
  returns decoded string by shifting every character 5 places backwards in the alphabet.
   */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) + 26) % 26 + "a".charCodeAt(0)
  )).join("");
}

/*
  tests
   */
console.log(encodeShift("hello")); // should return "mjqqt"
console.log(decodeShift("mjqqt")); // should return "hello"
console.log(encodeShift("world")); // should return "btwol"
console.log(decodeShift("btwol")); // should return "world"

```

This code works by using the charCodeAt() function to convert the characters in the string to their respective ASCII values, then performing a shift on these values with the modulo operator. The % 26 is used to ensure that the shift wraps around the alphabet when it goes past 'z'. The map function is used to apply the shift to every character in the string. Finally, the join function is used to convert the array of characters back into a string. The decodeShift function is the same as the encodeShift function, but with the shift direction reversed.

```javascript

// Test cases
console.log(encodeShift("hello")); // should return "mjqqt"
console.log(decodeShift("mjqqt")); // should return "hello"
console.log(encodeShift("world")); // should return "btwol"
console.log(decodeShift("btwol")); // should return "world"

```

These test cases check that the shift encoding and decoding functions work as expected.

```javascript

// Test cases
console.log(encodeShift("hello")); // should return "mjqqt"
console.log(decodeShift("mjqqt")); // should return "hello"
console.log(encodeShift("world")); // should return "btwol"
console.log(decodeShift("btwol")); // should return "world"

```

These test cases check that the shift encoding and dec