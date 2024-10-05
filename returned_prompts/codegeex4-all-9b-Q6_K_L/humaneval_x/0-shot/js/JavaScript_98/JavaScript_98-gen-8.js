You can use the `match` method to match uppercase vowels at even indices and then return the length of the resulting array. Here's the code:

```javascript
const countUpper = (s) => {
  const vowels = 'AEIOU';
  const evenIndices = s.match(/([AEIOU][a-z]*[A-Z])|([AEIOU])/g);
  return (evenIndices || []).filter((word) => vowels.includes(word[0])).length;
};
```

The `match` method is used to find all occurrences of uppercase vowels at even indices. The regular expression `/([AEIOU][a-z]*[A-Z])|([AEIOU])/g` matches either an uppercase vowel followed by any number of lowercase letters and an uppercase letter, or an uppercase vowel alone. The `filter` method is used to filter out any words that don't start with an uppercase vowel. Finally, the length of the resulting array is returned.