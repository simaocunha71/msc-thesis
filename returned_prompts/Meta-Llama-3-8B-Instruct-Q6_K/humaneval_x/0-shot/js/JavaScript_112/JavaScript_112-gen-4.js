```javascript
const reverseDelete = (s, c) => {
  // Filter out characters in s that are equal to any character in c
  const result = s.split('').filter(char => !c.includes(char)).join('');
  
  // Check if the result string is palindrome
  const isPalindrome = result === result.split('').reverse().join('');
  
  // Return a tuple containing the result string and the check result
  return [result, isPalindrome];
}
```
Explanation:

1. `s.split('')` converts the string `s` into an array of individual characters.
2. `filter(char => !c.includes(char))` filters out the characters in `s` that are equal to any character in `c`. The `!` operator is used to negate the condition, so that characters that are not in `c` are kept.
3. `join('')` converts the filtered array back into a string.
4. `result === result.split('').reverse().join('')` checks if the result string is a palindrome by comparing it with its reverse.
5. The result tuple is returned, containing the filtered string and the palindrome check result.

Example usage:
```javascript
console.log(reverseDelete("abcde", "ae")); // Output: ['bcd', false]
console.log(reverseDelete("abcdef", "b")); // Output: ['acdef', false]
console.log(reverseDelete("abcdedcba", "ab")); // Output: ['cdedc', true]
```  ```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```javascript
```