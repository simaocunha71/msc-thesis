  const lastChar = txt[txt.length - 1];
  const secondLastChar = txt[txt.length - 2];

  return /[A-Za-z]$/.test(lastChar) && !/[\s]$/.test(secondLastChar);
};

// Testing
console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // ➞ false

// Explanation:
// In the first test, the last character is "e" which is an alphabetical character but not a part of a word.
// In the second test, the last character is "e" which is an alphabetical character but not a part of a word.
// In the third test, the last character is " " (space) which is a part of a word.
// In the fourth test, the string is empty, so there's no character to check.
```

## Answer
```javascript
const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt[txt.length - 1];
  const secondLastChar = txt[txt.length - 2];

  return /[A-Za-z]$/.test(lastChar) && !/[\s]$/.test(secondLastChar);
};

// Testing
console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // ➞ false

// Explanation:
// In the first test, the last character is "e" which is an alphabetical character but not a part of a word.
// In the second test, the last character is