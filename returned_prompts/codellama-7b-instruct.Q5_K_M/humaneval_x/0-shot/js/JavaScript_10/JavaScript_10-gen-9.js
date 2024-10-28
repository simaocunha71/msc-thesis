/* Test if gniven strig is a palindrome */
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

/* Find the shortest palindrome that begins with a supplied string.
  Algorithm idea is simple:
  - Find the longest postfix of supplied string that is a palindrome.
  - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
  >>> makePalindrome('')
  ''
  >>> makePalindrome('cat')
  'catac'
  >>> makePalindrome('cata')
  'catac'
  */
const makePalindrome = (string) => {
  if (string.length === 0) {
    return string;
  }
  const postfix = string.split('').reverse().join('');
  if (isPalindrome(postfix)) {
    return string + postfix;
  }
  const prefix = string.slice(0, -1);
  const prefixReverse = prefix.split('').reverse().join('');
  return string + prefixReverse + postfix;
}

/*
Test with these calls:
  makePalindrome('racecar');
  makePalindrome('level');
  makePalindrome('civic');
  makePalindrome('radar');
  makePalindrome('');
*/
