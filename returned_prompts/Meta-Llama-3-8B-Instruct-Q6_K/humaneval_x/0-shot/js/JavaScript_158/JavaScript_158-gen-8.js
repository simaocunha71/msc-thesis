Here is the JavaScript function that meets the requirements:

```javascript
const findMax = (words) => {
  let maxUniqueChars = 0;
  let result = '';

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
```

In this function, we initialize `maxUniqueChars` to 0 and `result` to an empty string. Then, we iterate over the `words` array. For each word, we calculate the number of unique characters using a `Set`, which automatically removes duplicates. If the number of unique characters is greater than `maxUniqueChars`, we update `maxUniqueChars` and `result` to the current word. If the number of unique characters is equal to `maxUniqueChars`, we check if the current word is lexicographically smaller than `result` and update `result` if it is. Finally, we return `result`.