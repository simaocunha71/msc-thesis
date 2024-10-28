Here is the JavaScript solution for the problem:

```javascript
const vowelsCount = (s) => {
  let count = 0;
  let lastChar = '';
  for (let char of s.toLowerCase()) {
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
      count++;
    } else if (char === 'y' && lastChar === '') {
      count++;
    }
    lastChar = char;
  }
  return count;
};
```



This function works by iterating over the input string `s`, converting each character to lowercase, and checking if it's a vowel. If it's a vowel, it increments the `count` variable. If the character is 'y' and it's the last character in the string, it also increments the `count` variable. Finally, it returns the `count` variable, which represents the number of vowels in the input string. The last character is stored in the `lastChar` variable to keep track of whether the current character is the last one in the string. This is necessary because 'y' is considered a vowel only when it's at the end of the string.