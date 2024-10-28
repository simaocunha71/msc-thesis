```
const isPalindrome = (text) => text === text.split('').reverse().join('');
```



Explanation:

*   The function `isPalindrome` takes a string `text` as an argument.
*   It uses the `split` method to split the string into an array of individual characters.
*   It then uses the `reverse` method to reverse the order of the characters in the array.
*   Finally, it uses the `join` method to combine the characters back into a string.
*   The function then compares the original string with the reversed string. If they are the same, the function returns `true`, indicating that the string is a palindrome. Otherwise, it returns `false`.