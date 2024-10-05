  let count = 0;
  for (let i = 0; i < string.length; i++) {
    count++;
  }
  return count;
};

console.log(strlen('abc'));
console.log(strlen(''));

// Output:
// 3
// 0

// Explanation:
// The first string 'abc' has a length of 3, and the second string '' (empty string) has a length of 0.
// So we return 3 and 0 respectively.
```

## Question 2

Write a JavaScript function that determines if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.

```javascript
