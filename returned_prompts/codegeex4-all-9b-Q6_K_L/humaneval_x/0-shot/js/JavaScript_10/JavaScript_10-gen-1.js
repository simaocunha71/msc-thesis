Here is the complete solution:

```javascript
/* Test if given string is a palindrome */
const isPalindrome = (string) => {
  return string == string.split('').reverse().join('');
}

/* Find the shortest palindrome that begins with a supplied string.
  Algorithm idea is simple:
  - Find the longest postfix of supplied string that is a palindrome.
  - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
  */
const makePalindrome = (string) => {
  if (isPalindrome(string)) {
    return string;
  }
  for (let i = string.length - 1; i >= 0; i--) {
    let suffix = string.slice(i);
    let prefix = string.slice(0, i);
    if (isPalindrome(suffix)) {
      return suffix + prefix.split('').reverse().join('');
    }
  }
}
```

The `isPalindrome` function checks if a string is a palindrome by comparing it to its reverse.

The `makePalindrome` function creates the shortest palindrome that starts with the given string. It uses a loop to find the longest suffix of the string that is a palindrome. If it finds such a suffix, it appends the reverse of the prefix that comes before the palindromic suffix to the end of the string.

This solution has a time complexity of O(n^2) where n is the length of the string, because in the worst case we need to check all suffixes of the string.