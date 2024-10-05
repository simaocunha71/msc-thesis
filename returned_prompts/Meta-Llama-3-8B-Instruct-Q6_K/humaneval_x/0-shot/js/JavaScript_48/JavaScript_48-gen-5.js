```
const isPalindrome = (text) => {
  return text.split('').reverse().join('') === text;
};
```


Explanation:

*   We split the input string into an array of individual characters using the `split` method with an empty string as the separator.
*   We reverse the array using the `reverse` method.
*   We join the reversed array back into a string using the `join` method with an empty string as the separator.
*   We compare the resulting string with the original input string using the `===` operator.
*   If the two strings are the same, the function returns `true`, indicating that the input string is a palindrome. Otherwise, it returns `false`.