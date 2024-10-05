```javascript
const countUpper = (s) => {
  // Use the match method to find all uppercase vowels in even indices
  return (s.match(/[AEIOU]/g) || []).filter((char, index) => index % 2 === 0).length;
}
```

The match method returns an array of all matches of the regular expression in the string. We then filter this array to only include uppercase vowels at even indices, and finally return the length of this filtered array. If no matches are found, the match method returns null, so we use the logical OR operator to replace it with an empty array.