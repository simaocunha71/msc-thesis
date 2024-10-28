  const uniqueCharacters = new Set(string.toLowerCase());
  return [...uniqueCharacters].filter(character => character !== " ").length;
};

module.exports = countDistinctCharacters;

// Set automatically removes duplicates, so it's perfect for this task.
// Then we convert the set back to an array, filter out any spaces, and return the length of this array.
// The result is the number of distinct characters in the string.
// The time complexity is O(n), where n is the length of the string.
// The space complexity is also O(n), because in the worst case scenario (all characters are distinct), the set will have the same number of elements as the string.


```

## Solution 2:

```javascript
