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

In this function, we iterate through each character in the string using a for loop. We check if the current index is even using the condition `i % 2 === 0`. If it is, we check if the character at that index is an uppercase vowel by converting the character to uppercase and checking if it is in the array `['A', 'E', 'I', 'O', 'U']`. If it is, we increment the count. Finally, we return the count.