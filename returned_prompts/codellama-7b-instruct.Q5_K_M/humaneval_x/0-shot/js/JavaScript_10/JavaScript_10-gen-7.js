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
  // find the longest postfix that is a palindrome
  let postfix = string.split('').reverse().join('');
  while (!isPalindrome(postfix)) {
    postfix = postfix.substring(0, postfix.length - 1);
  }

  // find the prefix that comes before the palindromic suffix
  let prefix = string.substring(0, string.length - postfix.length);
  // append to the end of the string
  return string + prefix.split('').reverse().join('');
}


/* Test if given strig is a palindrome */
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
  // find the longest postfix that is a palindrome
  let postfix = string.split('').reverse().join('');
  while (!isPalindrome