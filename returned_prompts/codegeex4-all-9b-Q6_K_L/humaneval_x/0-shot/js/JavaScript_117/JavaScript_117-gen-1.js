Here is a possible solution in JavaScript:

```javascript
const selectWords = (s, n) => {
  if (s.trim() === '') return [];
  const words = s.split(' ');
  const vowels = ['a', 'e', 'i', 'o', 'u'];
  let result = [];
  for (let i = 0; i < words.length; i++) {
    let consonants = 0;
    for (let j = 0; j < words[i].length; j++) {
      if (!vowels.includes(words[i][j].toLowerCase())) {
        consonants++;
      }
    }
    if (consonants === n) {
      result.push(words[i]);
    }
  }
  return result;
};
```

This solution first checks if the input string `s` is empty or contains only spaces. If so, it returns an empty list.

If the string `s` is not empty, it splits the string into an array of words using the `split` method.

Then, it iterates through each word in the array and counts the number of consonants in each word. If the number of consonants in a word is equal to the given number `n`, it adds the word to the result array.

Finally, it returns the result array.