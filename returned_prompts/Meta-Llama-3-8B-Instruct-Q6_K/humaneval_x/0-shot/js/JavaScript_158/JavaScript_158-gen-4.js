```javascript
const findMax = (words) => {
  if (!words.length) return '';

  let maxUniqueChars = 0;
  let maxWord = '';

  words.forEach((word) => {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  });

  return maxWord;
};
```  // Your code here
```
Explanation:

1. First, we check if the input array is empty. If it is, we return an empty string.
2. We initialize two variables, `maxUniqueChars` and `maxWord`, to keep track of the word with the maximum number of unique characters and the word itself, respectively.
3. We iterate through each word in the input array.
4. For each word, we calculate the number of unique characters using the `Set` data structure.
5. If the number of unique characters is greater than the current maximum, we update `maxUniqueChars` and `maxWord`.
6. If the number of unique characters is equal to the current maximum, we check if the current word is lexicographically smaller than the current `maxWord`. If it is, we update `maxWord`.
7. Finally, we return the `maxWord`.

This solution has a time complexity of O(n), where n is the length of the input array, because we iterate through each word once. The space complexity is O(1), because we use a constant amount of space to store the variables.  // Your code here
```javascript
const findMax = (words) => {
  if (!words.length) return '';

  let maxUniqueChars = 0;
  let maxWord = '';

  words.forEach((word) => {
    const uniqueChars = new Set(word).size;
    if (uniqueChars > maxUniqueChars) {
      maxUniqueChars = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUniqueChars) {
      if (word < maxWord) {
        maxWord = word;
      }
    }
  });

  return maxWord;
};
```  // Your code here
```
Explanation:

1. First, we check if the input array is empty. If it is, we return an empty string.
