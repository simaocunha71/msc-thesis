  return number - Math.floor(number);
};

/* Given a string, it can be decomposed into a set of unique characters.

  Return the set of unique characters of the string.
  >>> uniqueChars('hello')
  {'h', 'e', 'l', 'o'}
  */
const uniqueChars = (string) => {
  let charSet = new Set();
  for (let char of string) {
    charSet.add(char);
  }
  return charSet;
};

/* Given two strings, return the longest common substring.
  (a substring is a contiguous sequence of characters within a string).

  >>> longestCommonSubstring('hello world', 'worldwide')
  'world'
  */
const longestCommonSubstring = (string1, string2) => {
  let longest = '';
  for (let i = 0; i < string1.length; i++) {
    let currentSubstring = '';
    for (let j = 0; j < string2.length; j++) {
      currentSubstring += string1[i];
      if (string2.includes(currentSubstring)) {
        if (currentSubstring.length > longest.length) {
          longest = currentSubstring;
        }
      } else {
        currentSubstring = '';
      }
    }
  }
  return longest;
};

/* Given a string, it can be decomposed into a set of unique characters.

  Return the set of unique characters of the string.
  >>> uniqueChars('hello')
  {'h', 'e', 'l', 'o'}
  */
const longestCommonPrefix = (string1, string2) => {
  let prefix = '';
  for (let i = 0; i < string1.length && i < string2.length; i++) {
    if (string1[i] !== string2[i]) {
      break;
    } else {
      prefix += string1[i];
    }
  }
  return prefix;
};

/* Given two strings, return the longest common substring.
  (a substring is a contiguous sequence of characters within a string).

