  return string.length;
};

/* Return the first index of a substring in the string
  >>> indexOf('', '')
  0
  >>> indexOf('abc', 'a')
  0
  >>> indexOf('abc', 'c')
  2
 */
const indexOf = (string, subString) => {
  let i = 0;
  while (i < string.length) {
    if (string.slice(i, i + subString.length) === subString) {
      return i;
    }
    i++;
  }
  return -1;
};

/* Return the last index of a substring in the string
  >>> lastIndexOf('', '')
  -1
  >>> lastIndexOf('abc', 'a')
  2
  >>> lastIndexOf('abc', 'c')
  0
 */
const lastIndexOf = (string, subString) => {
  let i = string.length;
  while (i--) {
    if (string.slice(i, i + subString.length) === subString) {
      return i;
    }
  }
  return -1;
};

/* Return if a string is a palindrome
  >>> isPalindrome('')
  true
  >>> isPalindrome('abc')
  false
  >>> isPalindrome('aba')
  true
 */
const isPalindrome = (string) => {
  const reversedString = string.split('').reverse().join('');
  return string === reversedString;
};

/* Return the substring from start to end (inclusive)
  >>> substring('abc', 1, 3)
  'bc'
 */
const substring = (string, start, end) => {
  return string.slice(start, end + 1);
};

/* Return a new string with all occurrences of the substring replaced by a replacement string
  >>> replace('abc', 'a', 'b')
  'bbc'
  >>> replace('abc', 'c', 'b')
  'abc'
 */
const replace = (string, subString, replacement) => {
  return string.split(subString).