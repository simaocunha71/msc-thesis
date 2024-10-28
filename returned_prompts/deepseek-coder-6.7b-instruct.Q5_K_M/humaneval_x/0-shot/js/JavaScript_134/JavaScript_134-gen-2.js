  const lastChar = txt[txt.length - 1];
  const penultimateChar = txt[txt.length - 2];

  return (
    /[a-zA-Z]/.test(lastChar) &&
    (penultimateChar === undefined || !/[a-zA-Z]/.test(penultimateChar))
  );
};

console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // ➞ false

/*
  The function first gets the last character and the penultimate character from the string.
  Then it checks if the last character is a letter using regular expression and if the penultimate character is not a letter.
  If both conditions are true, it returns true, otherwise it returns false.
*/
```

This function `checkIfLastCharIsALetter` takes a string as an argument, checks the last character of the string and returns true if the last character is a letter and the character before it is not a letter.

The function uses regular expressions to check if the character is a letter. If the last character is a letter and the penultimate character is not a letter, the function returns true. Otherwise, it returns false.

The function also handles the case where the string is empty, in which case the function also returns false.

## How to use this function

To use this function, simply call it with a string as an argument. The function will return a boolean value indicating whether the last character of the string is a letter and not a part of a word.

```javascript
console.log(checkIfLastCharIsALetter("apple pie")); // ➞ false
console.log(checkIfLastCharIsALetter("apple pi e")); // ➞ true
console.log(checkIfLastCharIsALetter("apple pi e  ")); // ➞ false
console.log(checkIfLastCharIsALetter("")); // 