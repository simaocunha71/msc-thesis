  const length = strings.length;
  let max = 0;
  let maxString = null;

  for (let i = 0; i < length; i++) {
    const string = strings[i];
    if (string.length > max) {
      max = string.length;
      maxString = string;
    }
  }

  return maxString;
};

/* Return an array of all substrings of the string. Note that this includes the whole string
  itself. For example, the substrings of "abcd" are ["abcd", "ab", "abc", "abd", "b", "bc", "bd", "cd", "d"].
  >>> substrings('')
  []
  >>> substrings('abc')
  ['abc', 'ab', 'ac', 'a', 'bc', 'b', 'c', '']
  >>> substrings('abcd')
  ['abcd', 'ab', 'abc', 'abd', 'b', 'bc', 'bd', 'cd', 'd']
  */
const substrings = (string) => {
  const result = [];

  for (let i = 0; i < string.length; i++) {
    for (let j = i; j < string.length; j++) {
      result.push(string.slice(i, j + 1));
    }
  }

  return result;
};

/* Return whether the given string is a palindrome. A palindrome is a string that remains the
  same when its characters are reversed, such as "madam" or "racecar". Note that the case of
  the letters matters. For example, "Able was I ere I saw Elba" is not a palindrome, but "A man, a plan, a canal, Panama!" is.
  >>> isPalindrome('')
  true
  >>> isPalindrome('abc')
  false
  >>> isPalindrome('madam')
  true
  >>> isPalindrome('racecar')
  true
  >>> isPalindrome('Able was I ere I saw Elba')
  false
  >>> isPalindrome('A man, a plan,