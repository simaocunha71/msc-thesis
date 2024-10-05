```js
/* Test if supplied string is a palindrome */
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
  if (isPalindrome(string)) {
    return string;
  }
  let postfix = string;
  while (postfix.length) {
    if (isPalindrome(postfix)) {
      let prefix = string.slice(0, string.length - postfix.length);
      return string + prefix.split('').reverse().join('');
    }
    postfix = postfix.slice(0, postfix.length - 1);
  }
}
```