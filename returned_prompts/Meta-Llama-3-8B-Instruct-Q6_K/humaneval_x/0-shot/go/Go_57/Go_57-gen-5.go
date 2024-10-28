Here is the solution using JavaScript:

```javascript
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];
  
  for (let word of words) {
    let consonants = 0;
    for (let char of word) {
      if (!['a', 'e', 'i', 'o', 'u', ' '].includes(char.toLowerCase())) {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(word);
    }
  }
  
  return result;
};
```

This function splits the input string into words, then iterates over each word. It counts the number of consonants in each word by checking if the character is not a vowel (a, e, i, o, u) or a space. If the count of consonants matches the given number `n`, the word is added to the result list. Finally, the function returns the list of words with the specified number of consonants.