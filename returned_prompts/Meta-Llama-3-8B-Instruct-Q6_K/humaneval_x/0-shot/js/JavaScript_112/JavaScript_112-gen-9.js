```javascript
const reverseDelete = (s, c) => {
  let result = s.split('').filter(char => !c.includes(char)).join('');
  let isPalindrome = result === result.split('').reverse().join('');
  return [result, isPalindrome];
};
```
Explanation:
1. We use the `split` method to convert the string `s` into an array of characters.
2. We use the `filter` method to create a new array that includes only the characters that are not present in the string `c`. We do this by checking if `char` (each character in the array) is not included in `c` using the `includes` method.
3. We use the `join` method to convert the filtered array back into a string, which is our result.
4. We use the `split` method again to split the result string into an array of characters.
5. We use the `reverse` method to reverse the array of characters.
6. We use the `join` method again to convert the reversed array back into a string.
7. We compare the result string with the reversed string to check if it is a palindrome. If they are the same, it is a palindrome.
8. We return a tuple containing the result string and a boolean indicating whether it is a palindrome. The boolean is set to `true` if the result string is a palindrome, and `false` otherwise.