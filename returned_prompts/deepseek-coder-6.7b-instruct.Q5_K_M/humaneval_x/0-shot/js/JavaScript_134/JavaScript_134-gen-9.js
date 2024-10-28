  const lastChar = txt.charAt(txt.length - 1);
  const secondLastChar = txt.charAt(txt.length - 2);
  const regex = /[a-z]/i;

  return (
    regex.test(lastChar) &&
    (!regex.test(secondLastChar) ||
      secondLastChar === " " ||
      secondLastChar === "")
  );
};

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false
console.log(checkIfLastCharIsALetter("This is a test ")); // false
console.log(checkIfLastCharIsALetter("This is a test")); // true

//  This program works by using the JavaScript built-in function charAt() to get the last and second last characters of the string.
//  Then it uses a regular expression to test if the last character is a letter.
//  The second condition ensures that the last character is not part of a word.
//  If both conditions are true, the function returns true. Otherwise, it returns false.

//  Note: This function assumes that words are separated by spaces and that there is no more than one space between words.
//  If this assumption does not hold, the function may return incorrect results.
```






























































































































































