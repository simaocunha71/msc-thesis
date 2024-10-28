/* Create a function that takes a string as an argument and returns true if the last character is a letter, and false otherwise.
  Examples:
  checkIfLastCharIsALetter("apple") ➞ true
  checkIfLastCharIsALetter("apple pie") ➞ false
  checkIfLastCharIsALetter("apple pi e") ➞ false
  checkIfLastCharIsALetter("apple pi e ") ➞ false
  checkIfLastCharIsALetter("") ➞ false
  */

const checkIfLastCharIsALetter = (txt) => {
  const lastChar = txt.slice(-1);
  return /^[A-Za-z]$/.test(lastChar);
}

