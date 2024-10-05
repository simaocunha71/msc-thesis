
function checkDictCase(dict) {
    let keys = Object.keys(dict);
    let lowerCase = keys.every(key => typeof key === 'string' && key.toLowerCase() === key);
    let upperCase = keys.every(key => typeof key === 'string' && key.toUpperCase() === key);
    return lowerCase || upperCase;
}

/*
  Given an array of strings, return true if all strings have the same length, else return false.
  Examples:
  sameLength(["a", "aa", "aaa"]) should return true.
  sameLength(["a", "aaay", "ay"]) should return false.
  sameLength(["a", "ay", "aaay"]) should return false.
*/
const sameLength = (arr) => {
  let length = arr[0].length;
  return arr.every(str => str.length === length);
};


/*
  Given an array of strings, return the longest string. If the array is empty, return an empty string.
  Examples:
  longestString(["a", "aa", "aaa"]) should return "aaa".
  longestString(["a", "aaay", "ay"]) should return "aaay".
  longestString(["a", "ay", "aaay"]) should return "aaay".
*/
const longestString = (arr) => {
  let longest = arr[0];
  arr.forEach(str => {
    if (str.length > longest.length) {
      longest = str;
    }
  });
  return longest;
};


/*
  Given an array of strings, return a new array with all strings sorted alphabetically in lower case.
  Examples:
  sortAlphabetically(["a", "ay", "aaay"]) should return ["a", "aaay", "ay"].
  sortAlphabetically(["A", "b", "ay"]) should return ["A", "a", "b"].
  sortAlphabetically(["Z", "Y", "X"]) should return ["X", "Y", "Z"].
*/
const sortAlphabetically = (arr) => {
  return arr.sort((a, b) => a.toLowerCase()