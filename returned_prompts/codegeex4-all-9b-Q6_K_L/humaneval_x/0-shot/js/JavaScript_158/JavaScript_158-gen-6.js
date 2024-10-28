To solve this problem, we need to find the word with the maximum number of unique characters. If multiple words have the same number of unique characters, we return the one that comes first in lexicographical order.

Here is the solution using JavaScript:

```javascript
const findMax = (words) => {
  // Initialize the maxUniqueCount and maxUniqueWord variables
  let maxUniqueCount = 0;
  let maxUniqueWord = "";

  // Iterate through each word in the list
  for (let word of words) {
    // Get the set of unique characters in the word
    let uniqueChars = new Set(word.split(""));
    let uniqueCount = uniqueChars.size;

    // If the current word has more unique characters than the maxUniqueCount,
    // update maxUniqueCount and maxUniqueWord
    if (uniqueCount > maxUniqueCount) {
      maxUniqueCount = uniqueCount;
      maxUniqueWord = word;
    }
    // If the current word has the same number of unique characters as the maxUniqueCount,
    // compare them lexicographically
    else if (uniqueCount === maxUniqueCount) {
      if (word < maxUniqueWord) {
        maxUniqueWord = word;
      }
    }
  }

  // Return the word with maximum number of unique characters
  return maxUniqueWord;
};
```

This solution has a time complexity of O(n*m), where n is the number of words in the list and m is the average length of the words.