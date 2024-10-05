```javascript
const histogram = (test) => {
  if (!test) return {};

  const wordArray = test.split(' ');
  const wordCounts = wordArray.reduce((acc, word) => {
    acc[word] = (acc[word] || 0) + 1;
    return acc;
  }, {});

  const maxCount = Math.max(...Object.values(wordCounts));
  const result = {};

  Object.keys(wordCounts).forEach((word) => {
    if (wordCounts[word] === maxCount) result[word] = maxCount;
  });

  return result;
};
```
Explanation:
- First, we split the input string into an array of words using the `split` method.
- Then, we use the `reduce` method to create an object where each key is a word and its value is the count of that word in the array.
- We find the maximum count using the `Math.max` function and the `Object.values` method.
- Finally, we iterate over the word counts object and add each word with the maximum count to the result object. If there are multiple words with the same maximum count, they are all added to the result object.

This solution has a time complexity of O(n), where n is the length of the input string, because we iterate over the input string twice (once to split it into words and once to count the words). The space complexity is O(n) as well, because we store the word counts in an object.