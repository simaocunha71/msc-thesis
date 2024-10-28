  let maxUnique = 0;
  let maxWord = '';

  for (const word of words) {
    const uniqueChars = new Set(word.split('')).size;
    if (uniqueChars > maxUnique) {
      maxUnique = uniqueChars;
      maxWord = word;
    } else if (uniqueChars === maxUnique) {
      maxWord = maxWord < word ? maxWord : word;
    }
  }

  return maxWord;
};

console.log(findMax(["name", "of", "string"]));
console.log(findMax(["name", "enam", "game"]));
console.log(findMax(["aaaaaaa", "bb", "cc"]));

```

## Notes

In this code, we initialize `maxUnique` to 0 and `maxWord` to an empty string. Then, for each word in the input array, we create a set of the characters in the word (to eliminate duplicates), and check if the size of the set is greater than `maxUnique`. If it is, we update `maxUnique` and `maxWord`. If the number of unique characters is the same as `maxUnique`, we compare the words and update `maxWord` if the current word comes before `maxWord` in lexicographical order. Finally, we return `maxWord`.

## Tests

Here are some tests that you can use to verify the correctness of your implementation:

```javascript
console.log(findMax(["name", "of", "string"])); // "string"
console.log(findMax(["name", "enam", "game"])); // "enam"
console.log(findMax(["aaaaaaa", "bb", "cc"])); // "aaaaaaa"
```

These tests cover a variety of cases, including words with different numbers of unique characters and words with the same number of unique characters.

## Complexity

The time complexity of this code is O(n*m), where n is the number of words and m is the average length of the words. This is because we iterate over each character of each word. The space complexity is O(n), as we