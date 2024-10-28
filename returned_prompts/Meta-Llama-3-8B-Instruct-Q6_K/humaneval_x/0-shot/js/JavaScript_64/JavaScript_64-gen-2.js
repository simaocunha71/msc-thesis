Here is the solution to the problem:

```javascript
const vowelsCount = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    const char = s[i].toLowerCase();
    if (char === 'a' || char === 'e' || char === 'i' || char === 'o' || char === 'u') {
      count++;
    } else if (char === 'y' && i === s.length - 1) {
      count++;
    }
  }
  return count;
};
```


The function `vowelsCount` takes a string `s` as input and returns the number of vowels in the string. It iterates over each character in the string, converting each character to lowercase for case-insensitive comparison. If the character is 'a', 'e', 'i', 'o', or 'u', it increments the `count` variable. If the character is 'y' and it's the last character in the string, it also increments the `count` variable. Finally, it returns the `count` variable, which represents the number of vowels in the string.