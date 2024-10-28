```
function isPalindrome(text) {
  return text === text.split('').reverse().join('');
}
```



This function works by comparing the original string with the reversed string. If they are the same, then the string is a palindrome.

Here's a breakdown of how it works:

* `text.split('')`: Splits the string into an array of individual characters.
* `reverse()`: Reverses the order of the characters in the array.
* `join('')`: Joins the characters in the array back into a string.

By comparing the original string with the reversed string, we can determine if the string is a palindrome. If the strings are the same, then the string is a palindrome, and the function returns `true`. Otherwise, it returns `false`.

For example, if we call the function with the string `'aba'`, it will split the string into an array `['a', 'b', 'a']`, reverse the array to get `['a', 'b', 'a']`, and then join the array back into a string `'aba'`. Since the original string is the same as the reversed string, the function will return `true`.