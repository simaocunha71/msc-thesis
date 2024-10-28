Here's how you might solve this problem in JavaScript:

```javascript
const isPalindrome = (string) => {
  return string === string.split('').reverse().join('');
}

const makePalindrome = (string) => {
  let palindrome = string;
  let i = 0;

  while (!isPalindrome(palindrome) && i < string.length) {
    palindrome = string[i] + palindrome + string[i];
    i++;
  }

  return palindrome;
}
```

This code first checks if the given string is a palindrome. If not, it takes the first character of the string, appends it to the end of the string and to the beginning of the string, then checks again. It continues this process until it finds a palindrome.