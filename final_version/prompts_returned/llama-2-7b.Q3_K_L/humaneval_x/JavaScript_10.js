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
  const shortestPalindromicPrefix = string.split('')[0];
  let longestPalindromicPostfix;
  
  if (!shortestPalindromicPrefix || !(isPalindrome(shortestPalindromicPrefix))) return '';

  while (string.length > shortestPalindromicPrefix.length) {
    const currentPosix = string.charAt(0);
  
    if (!(isPalindrome(currentPosix + shortestPalindromicPrefix))) break;
    
    const newShortestPalindromicPrefix = shortestPalindromicPrefix + currentPosix; 
    longestPalindromicPostfix = newShortestPalindromicPrefix.split('').reverse().join('');
  
    if (string.length >= newShortestPalindromicPrefix.length) {
      string = string.slice(0, -1);
    } else {
      break;
    }
  }
  
  return longestPalindromicPostfix + shortestPalindromicPrefix;
}
```