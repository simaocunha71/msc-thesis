```javascript
const findMax = (words) => {
  let maxUnique = 0;
  let maxWord = '';

  for (let word of words) {
    let uniqueChars = new Set(word).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUnique) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  }

  return maxWord;
};
```


Explanation:
This function iterates over each word in the input list. For each word, it calculates the number of unique characters by converting the word into a Set and getting its size. If the number of unique characters in the current word is greater than the maximum number of unique characters found so far, it updates the maximum number and the corresponding word. If the number of unique characters is equal to the maximum number, it checks the lexicographical order of the words and updates the maximum word if the current word is smaller. Finally, it returns the word with the maximum number of unique characters. If no word has unique characters, it returns an empty string.