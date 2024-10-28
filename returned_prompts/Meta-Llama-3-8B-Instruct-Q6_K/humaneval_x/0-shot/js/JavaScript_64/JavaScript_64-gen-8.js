Here is the solution:
```javascript
const vowelsCount = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    if (['a', 'e', 'i', 'o', 'u', 'y'].includes(s[i].toLowerCase())) {
      if (i === s.length - 1 && s[i].toLowerCase() === 'y') {
        count++;
      } else {
        count++;
      }
    }
  }
  return count;
};
```
Here's an explanation of the solution:

The function `vowelsCount` takes a string `s` as input and returns the number of vowels in the string.

The function uses a `for` loop to iterate through each character in the string.

For each character, it checks