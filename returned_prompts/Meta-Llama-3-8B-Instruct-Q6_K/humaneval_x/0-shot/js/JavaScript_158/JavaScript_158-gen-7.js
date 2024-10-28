Here is a JavaScript solution for the problem:

```javascript
const findMax = (words) => {
  if (!words.length) return '';

  let max = 0;
  let result = '';

  for (let word of words) {
    let uniqueChars = new Set(word);
    if (uniqueChars.size > max) {
      max = uniqueChars.size;
      result = word;
    } else if (uniqueChars.size === max) {
      if (word < result) {
        result = word;
      }
    }
  }

  return result;
};
```

Explanation:

1. We iterate over each word in the input list.
2. For each word, we create a Set of its unique characters.
3. We check if the size of the Set is greater than the current maximum. If it is, we update the maximum and the result.
4. If the size of the Set is equal to the current maximum, we check if the word is lexicographically smaller than the current result. If it is, we update the result.
5. Finally, we return the result.

This solution has a time complexity of O(n*m), where n is the number of words and m is the maximum length of a word. This is because we are iterating over each word and for each word, we are iterating over its characters. The space complexity is O(m), as we are using a Set to store the unique characters of each word.