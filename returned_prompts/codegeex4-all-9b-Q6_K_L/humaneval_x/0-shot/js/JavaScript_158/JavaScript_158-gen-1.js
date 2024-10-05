Here is the solution in JavaScript:

```javascript
const findMax = (words) => {
  let maxWord = '';
  let maxUniqueChar = 0;

  for (let word of words) {
    let uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChar) {
      maxUniqueChar = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChar) {
      maxWord = word < maxWord ? word : maxWord;
    }
  }

  return maxWord;
}
```

This function works by iterating over each word in the input list. For each word, it creates a set of unique characters and compares its size to the current maximum number of unique characters. If the size is greater than the current maximum, it updates the maximum and the word. If the size is equal to the current maximum, it compares the word to the current maximum and updates it if it is lexicographically smaller. Finally, it returns the word with the maximum number of unique characters.