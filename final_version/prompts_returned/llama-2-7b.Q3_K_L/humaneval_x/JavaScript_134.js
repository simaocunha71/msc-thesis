/* Create a function that returns true if the last character
  of a given string is an alphabetical character and is not
  a part of a word, and false otherwise.
  Note: "word" is a group of characters separated by space.
  Examples:
  checkIfLastCharIsALetter("apple pie") ➞ false
  checkIfLastCharIsALetter("apple pi e") ➞ true
  checkIfLastCharIsALetter("apple pi e ") ➞ false
  checkIfLastCharIsALetter("") ➞ false
  */
const checkIfLastCharIsALetter = (txt) => {
  let str = txt.toLowerCase();
  const length = str.length;
  if(str[length-1] === ' ')
    return true;
  if(!str[length-1].includes('a'))
    return false;
  else
    return true;
}

console.log(`${checkIfLastCharIsALetter("apple pie")}`); // false
console.log(`${checkIfLastCharIsALetter("apple pi e")}`); // true
console.log(`${checkIfLastCharIsALetter("apple pi e ")}`); // false
