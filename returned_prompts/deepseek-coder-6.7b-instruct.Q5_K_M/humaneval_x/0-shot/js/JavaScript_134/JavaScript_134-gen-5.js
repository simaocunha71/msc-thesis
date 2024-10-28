  return /\b[a-z]$/i.test(txt);

};
console.log(checkIfLastCharIsALetter("apple pie"));
console.log(checkIfLastCharIsALetter("apple pi e"));
console.log(checkIfLastCharIsALetter("apple pi e "));
console.log(checkIfLastCharIsALetter(""));

/*
  Explanation:
  The function `checkIfLastCharIsALetter` takes a string `txt` as an argument.
  It uses a regular expression to test whether the last character of `txt` is a letter.
  The regular expression `/[a-z]$/i` matches any character that is a letter at the end of the string.
  The `\b` is a word boundary, ensuring that the letter is not part of a word.
  The `^` means the start of the line.
  The `$` means the end of the line.
  The `i` flag makes the regex case insensitive.
  The `.test` method returns true if the string matches the regex, and false otherwise.
  So, the function returns the result of this test.
 */

// Test cases:
// checkIfLastCharIsALetter("apple pie") ➞ false
// checkIfLastCharIsALetter("apple pi e") ➞ true
// checkIfLastCharIsALetter("apple pi e  ") ➞ false
// checkIfLastCharIsALetter("") ➞ false
// checkIfLastCharIsALetter(" ") ➞ false
// checkIfLastCharIsALetter("1234567890") ➞ false
// checkIfLastCharIsALetter("apple pi e 9") ➞ true
// checkIfLastCharIsALetter("apple pi e A") ➞ false
// checkIfLastCharIsALetter("apple pi e a") ➞ true

/*
  This function can be used to check the last character of a string if it is an alphabetical character and is not a part of a word.
 */










