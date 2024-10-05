  let neg = Infinity;
  let pos = Infinity;

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0 && lst[i] < neg) {
      neg = lst[i];
    } else if (lst[i] > 0 && lst[i] < pos) {
      pos = lst[i];
    }
  }

  return [neg === Infinity ? null : neg, pos === Infinity ? null : pos];
};


/* Create a function that takes an array of strings and returns a
  new array where all the strings in the original array have been
  capitalized.
  Examples:
  capitalizeStrings(['hello', 'world']) == ['HELLO', 'WORLD']
  capitalizeStrings([]) == []
  */
const capitalizeStrings = (strs) => {
  return strs.map(str => str.toUpperCase());
};


/* Create a function that takes a string of text and returns a
  new string where all the vowels have been removed.
  Examples:
  removeVowels('hello') == 'hll'
  removeVowels('') == ''
  */
const removeVowels = (str) => {
  let vowels = 'aeiou';
  return str.replace(/[aeiou]/g, '');
};


/* Create a function that takes a string of text and returns a
  new string where all the consonants have been removed.
  Examples:
  removeConsonants('hello') == 'o'
  removeConsonants('') == ''
  */
const removeConsonants = (str) => {
  let vowels = 'aeiou';
  return str.replace(/[^aeiou]/g, '');
};


/* Create a function that takes an array of numbers and returns a
  new array where all the negative numbers have been removed.
  Examples:
  filterOutNegatives([-2, 3, -4, 5, -6, 7]) == [3, 5, 7]
  filterOutNegatives