function splitString(s) {
  return s.split(/[\s,]+/);
}

console.log(splitString("Hi, my name is John")); // ["Hi", "my", "name", "is", "John"]
console.log(splitString("One, two, three, four, five, six")); // ["One", "two", "three", "four", "five", "six"]

// Alternative solution:
const wordsString = (s) => s.split(/[\s,]+/);
console.log(wordsString("Hi, my name is John")); // ["Hi", "my", "name", "is", "John"]
console.log(wordsString("One, two, three, four, five, six")); // ["One", "two", "three", "four", "five", "six"]

*/


/*
  The next task is to take an array of strings, and return a new array with all
  the words from the original array, but with the vowels removed.

  For example:
  filterVowels(["cat", "dog", "mouse", "elephant"]) ==
  ["ct", "dg", "mse", "lphnt"]

  filterVowels(["Hello", "World"]) == ["Hll", "Wrld"]

*/

const filterVowels = (words) => {
  return words.map((word) => {
    return word.replace(/[aeiou]/gi, '');
  });
}

console.log(filterVowels(["cat", "dog", "mouse", "elephant"])); // ["ct", "dg", "mse", "lphnt"]
console.log(filterVowels(["Hello", "World"])); // ["Hll", "Wrld"]






/*
  The next task is to take an array of strings, and return a new array with all
  the words from the original array, but with the consonants removed.

  For example:
  filterConsonants(["cat", "dog", "mouse", "elephant"]) ==
  ["a", "o", "ae", "ph"]

  filterConsonants(["