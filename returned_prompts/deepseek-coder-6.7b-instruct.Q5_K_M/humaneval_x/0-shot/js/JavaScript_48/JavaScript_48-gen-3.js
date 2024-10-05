  const reversedText = text.split('').reverse().join('');
  return text === reversedText;
};

console.log(isPalindrome('')); // true
console.log(isPalindrome('aba')); // true
console.log(isPalindrome('aaaaa')); // true
console.log(isPalindrome('zbcd')); // false

```

## Exercise 2:

Write a JavaScript function named `toUpperCase` that takes in a string and returns the same string but all in upper case.

```javascript
