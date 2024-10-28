Here is a JavaScript function that implements the desired behavior:

```javascript
const findMax = (words) => {
  let maxWord = '';
  let maxUniqueChars = 0;

  for (let word of words) {
    let uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxWord = word;
      maxUniqueChars = uniqueChars;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }

  return maxWord;
};
```
This function iterates over the list of words. For each word, it counts the number of unique characters using a Set. If the number of unique characters is greater than the current maximum, it updates the maximum word and the maximum number of unique characters. If the number of unique characters is equal to the current maximum, it checks if the word comes before the current maximum word in lexicographical order. If it does, it updates the maximum word. Finally, it returns the maximum word. If no word has unique characters, it returns an empty string. 