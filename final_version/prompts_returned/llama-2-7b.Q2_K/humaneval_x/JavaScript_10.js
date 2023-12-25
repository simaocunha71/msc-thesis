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
  const isPalindromicPrefix = (prefix, n) => n >= prefix.length - 1 && isPalindrome(n);

  return Math.min(...Array.from(new Set([...string.split('')].map((str) => str + ''))).reverse()
    .filter((sub) => isPalindromicPrefix(sub, sub.length))
    .reduce((acc, n) => acc > n ? n : acc, string));
}
