Here is a JavaScript function that accomplishes the task:
```javascript
const reverseDelete = (s, c) => {
  // Create a new string with all characters in s that are not in c
  let result = '';
  for (let char of s) {
    if (!c.includes(char)) {
      result += char;
    }
  }
  
  // Check if the result string is a palindrome
  let isPalindrome = true;
  for (let i = 0; i < result.length / 2; i++) {
    if (result[i] !== result[result.length - i - 1]) {
      isPalindrome = false;
      break;
    }
  }
  
  return [result, isPalindrome];
};

// Test cases
console.log(reverseDelete("abcde", "ae")); // Output: ["bcd", false]
console.log(reverseDelete("abcdef", "b")); // Output: ["acdef", false]
console.log(reverseDelete("abcdedcba", "ab")); // Output: ["cdedc", true]
```
This function works by iterating over the characters in `s` and checking if each character is not in `c`. If it's not, it adds it to the result string. Then, it checks if the result string is a palindrome by comparing characters from the start and end of the string, moving towards the center. If any pair of characters don't match, it sets `isPalindrome` to `false`. Finally, it returns the result string and the `isPalindrome` flag as a tuple.