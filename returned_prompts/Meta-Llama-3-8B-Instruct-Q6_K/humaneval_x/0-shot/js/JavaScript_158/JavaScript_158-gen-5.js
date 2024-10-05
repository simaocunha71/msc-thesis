```javascript
const findMax = (words) => {
  let result = '';
  let maxUniqueChars = 0;

  for (let word of words) {
    let uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      result = word;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < result) {
        result = word;
      }
    }
  }
  return result;
};
```A: This function iterates over each word in the list. For each word, it calculates the number of unique characters using the Set data structure. If the number of unique characters is greater than the current maximum, it updates the result and the maximum number of unique characters. If the number of unique characters is equal to the current maximum, it checks if the word is lexicographically smaller than the current result and updates the result if necessary. At the end, it returns the result. If no word has unique characters, it returns an empty string. This solution has a time complexity of O(n*m), where n is the number of words and m is the maximum length of a word. It has a space complexity of O(m), for storing the Set of characters in the worst case. It works correctly for the given test cases.