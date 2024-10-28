Here is a JavaScript function that finds the shortest palindrome that begins with a supplied string:

```javascript
function makePalindrome(string) {
  // if string is empty then return empty string
  if (string === "") {
    return string;
  }

  // get the longest palindrome postfix
  const palindromePostfix = getPalindromePostfix(string);

  // get the prefix of string before the palindromic postfix
  const prefix = string.slice(0, string.length - palindromePostfix.length);

  // get the reversed prefix
  const reversedPrefix = prefix.split('').reverse().join('');

  // append the reversed prefix to the palindromic postfix
  const result = palindromePostfix + reversedPrefix;

  return result;
}

function getPalindromePostfix(string) {
  let i = string.length;
  while (i > 0) {
    const palindrome = string.slice(0, i) + string.slice(i).split('').reverse().join('');
    if (isPalindrome(palindrome)) {
      return palindrome;
    }
    i--;
  }
  return '';
}
```

In this function, we first check if the input string is empty. If it is, we simply return the empty string.

Next, we find the longest palindrome postfix of the input string using the `getPalindromePostfix` function. This function iteratively tries to extend the postfix with the first letter of the string, until it finds a palindrome. It returns the longest palindrome postfix found.

Then, we get the prefix of the string before the palindromic postfix using the `slice` method.

After that, we reverse the prefix using the `split` and `reverse` methods, and then join the characters back together using the `join` method. This gives us the reversed prefix.

Finally, we append the reversed prefix to the palindromic postfix and return the result.

Overall, this function finds the shortest palindrome that begins with the supplied string by appending the reversed prefix