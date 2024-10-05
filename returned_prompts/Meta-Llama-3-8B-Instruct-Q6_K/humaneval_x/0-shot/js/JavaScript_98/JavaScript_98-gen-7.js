Here is a JavaScript solution for the problem:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (i % 2 === 0 && s[i].toUpperCase() === 'A' || s[i].toUpperCase() === 'E' || s[i].toUpperCase() === 'I' || s[i].toUpperCase() === 'O' || s[i].toUpperCase() === 'U') {
      count++;
    }
  }
  return count;
};
```

This function iterates over the string using a for loop. It checks if the index is even (i % 2 === 0) and if the character at that index is an uppercase vowel (using the toUpperCase method and checking for the characters 'A', 'E', 'I', 'O', and 'U'). If both conditions are met, it increments the count. Finally, it returns the count.