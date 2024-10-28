```javascript
const countUpper = (s) => {
  return s
    .split('')
    .filter((char, i) => i % 2 === 0 && char.match(/[AEIOU]/i))
    .length;
};
```

Explanation:
1. `split('')`: This splits the string into an array of individual characters.
2. `filter((char, i) => i % 2 === 0 && char.match(/[AEIOU]/i))`: This filters out the characters that are at even indices and are uppercase vowels. The regular expression `/[AEIOU]/i` matches uppercase vowels, and `i % 2 === 0` checks if the index is even.
3. `.length`: This returns the length of the filtered array, which is the count of uppercase vowels at even indices.