Here is a JavaScript function that counts the number of uppercase vowels in even indices of a given string:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && ['A', 'E', 'I', 'O', 'U'].includes(s[i].toUpperCase())) {
      count++;
    }
  }
  return count;
};
```

This function uses a for loop to iterate over the characters in the string. It checks if the current index is even (i % 2 === 0) and if the character is an uppercase vowel (using the `includes` method and the `toUpperCase` method to convert the character to uppercase). If both conditions are met, it increments the count. Finally, it returns the count.