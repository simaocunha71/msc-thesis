/* Test if given string is a palindrome */
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
  // find the longest postfix of the string that is a palindrome
  const postfix = string.split('').reverse().join('');
  const longestPostfix = postfix.match(/((.(?!\1))*\1)/);
  // find the string prefix that comes before the palindromic suffix
  const prefix = string.slice(0, string.length - longestPostfix[0].length);
  // make the palindrome by appending the reverse of the prefix to the end of the string
  return string + prefix.split('').reverse().join('');
}
