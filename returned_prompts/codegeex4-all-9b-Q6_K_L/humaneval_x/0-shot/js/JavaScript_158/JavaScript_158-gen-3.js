```js
const findMax = (words) => {
  let maxUnique = 0
  let maxWord = ''

  for (let word of words) {
    const uniqueChars = new Set(word).size
    if (uniqueChars > maxUnique || (uniqueChars === maxUnique && word < maxWord)) {
      maxUnique = uniqueChars
      maxWord = word
    }
  }

  return maxWord
}
```

Explanation:
1. We initialize `maxUnique` to 0 and `maxWord` to an empty string.
2. We iterate over each word in the list.
3. For each word, we create a new Set from the characters in the word and get the size of the Set. This gives us the number of unique characters in the word.
4. If the number of unique characters in the word is greater than `maxUnique` or if it is equal to `maxUnique` but the word comes before `maxWord` in lexicographical order, we update `maxUnique` and `maxWord` accordingly.
5. Finally, we return `maxWord`, which is the word with the maximum number of unique characters.