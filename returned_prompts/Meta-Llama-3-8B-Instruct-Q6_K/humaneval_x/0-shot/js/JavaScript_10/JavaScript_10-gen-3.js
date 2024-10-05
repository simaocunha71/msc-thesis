```javascript
function makePalindrome(str) {
  let reversed = str.split('').reverse().join('');
  let prefix = '';
  let postfix = '';

  for (let i = 0; i < str.length; i++) {
    prefix = str.substring(0, i + 1);
    postfix = reversed.substring(reversed.length - i - 1);
    if (isPalindrome(prefix + postfix)) {
      return prefix + postfix;
    }
  }

  return str + reversed;
}

function isPalindrome(str) {
  return str === str.split('').reverse().join('');
}
```

Explanation:
The `makePalindrome` function works by iterating through the input string from left to right, and for each character, it checks if the prefix of the string and the reversed postfix of the string are a palindrome. If they are, it returns the resulting string. If no palindrome is found, it appends the reversed string to the end of the input string.

The `isPalindrome` function is a helper function that checks if a given string is a palindrome. It does this by comparing the string with its reverse. If they are the same, the string is a palindrome.

The `makePalindrome` function uses the `isPalindrome` function to check if the prefix and postfix of the string are a palindrome. If they are, it returns the resulting string. If no palindrome is found, it appends the reversed string to the end of the input string. This ensures that the resulting string is the shortest palindrome that begins with the input string.