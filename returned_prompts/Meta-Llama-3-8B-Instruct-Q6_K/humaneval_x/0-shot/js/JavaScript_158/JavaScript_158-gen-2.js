Here is the solution:

```javascript
const findMax = (words) => {
  let maxUniqueChars = 0;
  let result = '';

  words.forEach(word => {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      result = word;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < result) {
        result = word;
      }
    }
  });

  return result;
};
```

Explanation:

*   We initialize `maxUniqueChars` to 0 and `result` to an empty string.
*   We iterate through the `words` array using `forEach`.
*   For each word, we create a `Set` from the word and get its size using `size`. This gives us the number of unique characters in the word.
*   If the number of unique characters in the current word is greater than `maxUniqueChars`, we update `maxUniqueChars` and set `result` to the current word.
*   If the number of unique characters is equal to `maxUniqueChars`, we check if the current word is lexicographically smaller than `result`. If it is, we update `result`.
*   Finally, we return `result`, which is the word with the maximum number of unique characters in lexicographical order. If no word has unique characters, the function returns an empty string.