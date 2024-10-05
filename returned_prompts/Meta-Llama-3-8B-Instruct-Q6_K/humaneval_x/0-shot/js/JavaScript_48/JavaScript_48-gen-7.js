```
const isPalindrome = (text) => {
  return text === text.split('').reverse().join('');
};
```
This solution works by comparing the original string with the reversed string. If they are the same, then the string is a palindrome. The `split('')` function splits the string into an array of individual characters, `reverse()` reverses the array, and `join('')` joins the array back into a string. The `===` operator checks if the original string is equal to the reversed string. If they are equal, the function returns `true`, indicating that the string is a palindrome. If they are not equal, the function returns `false`.