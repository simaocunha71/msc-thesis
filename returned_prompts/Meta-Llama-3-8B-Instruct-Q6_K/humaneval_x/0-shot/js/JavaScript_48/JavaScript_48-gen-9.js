```
const isPalindrome = (text) => {
  return text === text.split('').reverse().join('');
};
```


Explanation:
The code checks if the given string is the same when its characters are reversed. It does this by splitting the string into an array of individual characters, reversing the array, and then joining the characters back into a string. If the resulting string is the same as the original string, then the string is a palindrome.

The time complexity is O(n), where n is the length of the string, because we are iterating over the string once to split it and once to reverse it. The space complexity is also O(n), because we are storing the characters of the string in an array.