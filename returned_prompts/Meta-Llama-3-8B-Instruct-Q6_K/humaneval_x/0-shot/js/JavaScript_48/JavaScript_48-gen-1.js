```javascript
const isPalindrome = (text) => {
  return text === text.split('').reverse().join('');
};
```


Explanation:
This function works by comparing the original string with the reversed string. The `split('')` method splits the string into an array of individual characters. The `reverse()` method reverses the order of the characters in the array. The `join('')` method combines the characters back into a string. If the original string is the same as the reversed string, then the string is a palindrome. If not, then it's not a palindrome. The `return` statement at the end of the function returns a boolean value indicating whether the string is a palindrome or not.