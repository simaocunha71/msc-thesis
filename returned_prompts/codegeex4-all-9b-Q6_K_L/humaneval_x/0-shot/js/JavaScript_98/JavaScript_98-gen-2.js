You can solve this problem by iterating over the string and checking if the character is an uppercase vowel and if its index is even. Here's how you can do it in JavaScript:

```javascript
const countUpper = (s) => {
  let count = 0;
  for (let i = 0; i < s.length; i += 2) {
    if (s[i] === 'A' || s[i] === 'E' || s[i] === 'I' || s[i] === 'O' || s[i] === 'U') {
      count++;
    }
  }
  return count;
}
```

In this code, we use a for loop to iterate over the string, incrementing the index by 2 to only check even indices. We then check if the character at the current index is an uppercase vowel by comparing it to each of the uppercase vowels. If it is, we increment the count. Finally, we return the count.