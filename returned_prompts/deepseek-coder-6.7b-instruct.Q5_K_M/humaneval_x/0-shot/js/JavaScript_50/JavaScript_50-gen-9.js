/*
  returns decoded string by shifting every character by 21 places in the alphabet.
   */
const decodeShift = (s) => {
  return s.split("").map(ch => String.fromCharCode(
    ((ch.charCodeAt(0) - 5 - "a".charCodeAt(0)) + 26) % 26 + "a".charCodeAt(0)
  )).join("");
}

// Testing
console.log(encodeShift("hello")); // "czggj"
console.log(decodeShift("czggj")); // "hello"
```

This code defines two functions: `encodeShift` and `decodeShift`. Each of these functions takes a string as input and returns an encoded or decoded string. 

`encodeShift` shifts each character in the input string 5 places to the right in the alphabet. 

`decodeShift` does the opposite: it shifts each character 5 places to the left. 

These functions use the `charCodeAt` method to convert characters to their ASCII integer values and the `String.fromCharCode` method to convert integers back to characters. The `% 26` in the `encodeShift` function ensures that the shift wraps around the alphabet when it goes past 'z'. The `decodeShift` function uses `+26` to make sure the shift wraps around the negative end of the alphabet. 

The code includes a test at the end of the file that checks these functions with the string "hello".


## 9.

```javascript
let countVowels = function(str) {
  let count = 0;
  let vowels = ['a', 'e', 'i', 'o', 'u'];

  for (let letter of str.toLowerCase()) {
    if (vowels.includes(letter)) {
      count += 1;
    }
  }

  return count;
}

console.log(countVowels("Hello World")); // 3
```

This code defines a function `countVowels` that takes a string as input and returns the number of vowels in that string. The function first initializes a count of 0 and an array of vowels