```
const isPalindrome = (text) => {
  return text === text.split('').reverse().join('');
};
```


Explanation:
The function takes a string as an argument and checks if it is a palindrome. A palindrome is a string that reads the same backward as forward.

The function uses the `split` method to split the string into an array of individual characters, the `reverse` method to reverse the order of the array, and the `join` method to concatenate the characters back into a string.

The function then compares the original string with the reversed string. If they are the same, the function returns `true`, indicating that the string is a palindrome. If they are not the same, the function returns `false`, indicating that the string is not a palindrome.

For example, the string `'aba'` is a palindrome because it reads the same backward as forward. The string `'zbcd'` is not a palindrome because it does not read the same backward as forward.