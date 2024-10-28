Here is the solution in JavaScript:

```javascript
const reverseDelete = (s, c) => {
    // create a new string without characters in c
    let result = s.split('').filter(char => !c.includes(char)).join('');
    // check if the result string is palindrome
    let isPalindrome = result === result.split('').reverse().join('');
    return [result, isPalindrome];
};

// test the function
console.log(reverseDelete("abcde", "ae")); // Output: ["bcd", false]
console.log(reverseDelete("abcdef", "b")); // Output: ["acdef", false]
console.log(reverseDelete("abcdedcba", "ab")); // Output: ["cdedc", true]
```
In this solution, we first filter the characters in the string `s` to exclude any characters that are in the string `c`. Then we check if the resulting string is a palindrome by comparing it to its reverse. If it is the same, then it is a palindrome. We return the result string and a boolean indicating whether it is a palindrome.