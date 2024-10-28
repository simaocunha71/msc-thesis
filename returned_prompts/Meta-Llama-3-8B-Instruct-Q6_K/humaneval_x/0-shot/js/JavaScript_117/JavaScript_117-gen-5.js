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

This function splits the input string into words using the `split` method, then iterates over each word. For each word, it counts the number of consonants using a loop that checks if the character is not a vowel (i.e., 'a', 'e', 'i', 'o', 'u', or a space). If the number of consonants matches the input number `n`, it adds the word to the result array. Finally, it returns the result array.