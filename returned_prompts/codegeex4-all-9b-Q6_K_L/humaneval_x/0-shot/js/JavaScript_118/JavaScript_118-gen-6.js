Here's one possible implementation:

```javascript
const getClosestVowel = (word) => {
  const vowels = 'aeiouAEIOU';
  for (let i = word.length - 1; i > 0; i--) {
    const currentChar = word[i];
    const previousChar = word[i - 1];
    if (vowels.includes(currentChar) && !vowels.includes(previousChar)) {
      return currentChar;
    }
  }
  return '';
}
```

This function iterates through the characters of the word from right to left, and checks if the current character is a vowel and the previous character is not a vowel. If it finds such a pair, it returns the current character. If it doesn't find any such pair, it returns an empty string.