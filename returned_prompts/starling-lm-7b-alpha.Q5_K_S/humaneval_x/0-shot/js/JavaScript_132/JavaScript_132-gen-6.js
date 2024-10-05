const openBrackets = /\[\(<{/;
const closeBrackets = /\]>\)}/;

return new RegExp(`(${openBrackets})(${closeBrackets})`).test(string);
};

// Alternative solution
const isNested = (str) => {
  let openCount = 0;
  for (let i = 0; i < str.length; i++) {
    if (str.charAt(i) === "[" || str.charAt(i) === "(" || str.charAt(i) === "{") {
      openCount++;
    } else if (str.charAt(i) === "]" || str.charAt(i) === ")" || str.charAt(i) === "}") {
      openCount--;
    }
    if (openCount < 0) {
      return false;
    }
  }
  return openCount === 0;
};

*/

/*
  Create a function that takes a string and a number as input and returns the number of times the string occurs in the input string.
  countSubStringOccurrence('hello', 'ell') ➞ 2
  countSubStringOccurrence('hello world', 'lo') ➞ 2
  countSubStringOccurrence('hello world', 'llo') ➞ 1
  countSubStringOccurrence('hello world', 'lol') ➞ 0
  countSubStringOccurrence('hello world', 'h') ➞ 1
*/

const countSubStringOccurrence = (str, subStr) => {
  let count = 0;
  let i = 0;

  while (i < str.length) {
    let j = i;
    while (j < str.length) {
      if (str.substring(i, j + 1) === subStr) {
        count++;
        i = j + 1;
        break;
      }
      j++;
    }
    i++;
  }

  return count;
};

// Alternative solution
function countSubStringOccurrence(str, subStr)