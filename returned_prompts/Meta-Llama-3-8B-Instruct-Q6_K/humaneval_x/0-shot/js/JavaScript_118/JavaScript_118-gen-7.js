Here is a JavaScript solution for the problem:

```javascript
const getClosestVowel = (word) => {
  for (let i = word.length - 1; i > 0; i--) {
    if (
      'aeiouAEIOU'.includes(word[i]) &&
      'aeiouAEIOU'.includes(word[i - 1]) === false &&
      'aeiouAEIOU'.includes(word[i + 1]) === false
    ) {
      return word[i];
    }
  }
  return '';
};
```

The function iterates over the word from right to left. It checks if the current character is a vowel and the previous and next characters are not vowels. If it finds such a vowel, it returns that vowel. If it doesn't find any such vowel, it returns an empty string. The function is case-insensitive because it converts all characters to lowercase or uppercase before checking.