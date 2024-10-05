  const lastChar = txt[txt.length - 1];
  return /[a-z]/i.test(lastChar) && txt[txt.length - 2] === ' ';
};

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false

In this solution, we first get the last character of the string. Then we test if it is an alphabetical letter using a regular expression. We also check if the second last character is a space, which indicates that it's not part of a word. If both conditions are met, the function returns true; otherwise, it returns false.
*/

const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt[txt.length - 1];
  return /[a-z]/i.test(lastChar) && txt[txt.length - 2] === ' ';
};

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false


/*
The function `checkIfLastCharIsALetter` takes a string `txt` as an argument. It checks the last character of the string. If it is an alphabet letter and the character before it is a space, the function returns `true`. Otherwise, it returns `false`.

Here is what happens in the function:

1. `const lastChar = txt[txt.length - 1];` - This line of code assigns the last character of the string to the variable `lastChar`.

2. `/[a-z]/i.test(lastChar)` - This line of code uses a regular expression to test if `lastChar` is an alphabet letter (either uppercase or lowercase). The `i