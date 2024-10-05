```javascript
const findMax = (words) => {
  let max = "";
  let maxCount = 0;
  for (let word of words) {
    let uniqueCount = new Set(word).size;
    if (uniqueCount > maxCount) {
      max = word;
      maxCount = uniqueCount;
    } else if (uniqueCount === maxCount) {
      if (word.localeCompare(max) < 0) {
        max = word;
      }
    }
  }
  return max;
};
```


Explanation:

1. Initialize `max` as an empty string and `maxCount` as 0. These will hold the result.

2. Iterate over the list of words using a `for...of` loop.

3. For each word, calculate the number of unique characters using the `Set` object. This is done by converting the word to a set (which removes duplicates) and then getting the size of the set.

4. If the unique count of the current word is greater than `maxCount`, update `max` to the current word and `maxCount` to the unique count.

5. If the unique count of the current word is equal to `maxCount`, compare the current word with `max` lexicographically using the `localeCompare` method. If the current word is smaller, update `max` to the current word.

6. After iterating over all words, `max` will hold the word with maximum number of unique characters, or the first one if multiple words have the same maximum number of unique characters.

7. Return `max`. If no word has unique characters, the function will return an empty string.