```
const isPalindrome = (text) => {
  return text === text.split('').reverse().join('');
};
```



Explanation:

*   The function `isPalindrome` takes a string `text` as input.
*   It uses the `split` method to split the string into an array of individual characters.
*   The `reverse` method is used to reverse the order of the characters in the array.
*   The `join` method is used to concatenate the characters in the reversed array back into a string.
*   The function then compares the original string with the reversed string using the `===` operator.
*   If the two strings are the same, the function returns `true`, indicating that the string is a palindrome.
*   If the two strings are not the same, the function returns `false`, indicating that the string is not a palindrome.

This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over the characters in the string once to split and reverse them, and once to join them back together. The space complexity is also O(n), because it uses an array to store the characters in the string.