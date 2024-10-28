To solve this Kata, we need to follow these steps:

1. Check if the last character of the given string is an alphabetical character or not. We can do this by using the `slice` method to get the last character of the string, and then check if it's an alphabet using the `isAlphabetic` function. We can use the `String.prototype.isAlphabetic` function to check if the last character is an alphabet.

2. If the last character is an alphabet, we need to check if it's part of a word or not. To do this, we can use the `split` method to split the string into an array of words, and then check if the last character is part of the last word in the array. We can use the `includes` method to check if the last character is part of the last word in the array.

3. If the last character is an alphabet and not part of a word, return true. Otherwise, return false.

Here's the implementation of the `checkIfLastCharIsALetter` function:

function checkIfLastCharIsALetter(txt) {
  const lastChar = txt.slice(-1);

  if (lastChar.isAlphabetic) {
    const words = txt.split(' ');
    return !words[words.length - 1].includes(lastChar);
  }

  return false;
}

You can test the function with the provided examples:

console.log(checkIfLastCharIsALetter("apple pie")); // false
console.log(checkIfLastCharIsALetter("apple pi e")); // true
console.log(checkIfLastCharIsALetter("apple pi e ")); // false
console.log(checkIfLastCharIsALetter("")); // false

*/

function checkIfLastCharIsALetter(txt) {
  const lastChar = txt.slice(-1);

  if (lastChar.isAlphabetic) {
    const words = txt.split(' ');
    return !words[words.length - 1].includes(lastChar);
  }

  return false;
}

console.log(checkIfLastCharIsALet