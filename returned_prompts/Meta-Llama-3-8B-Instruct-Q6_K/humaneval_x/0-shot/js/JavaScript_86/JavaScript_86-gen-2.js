Here is a JavaScript function that solves the problem:

```javascript
const antiShuffle = (s) => {
  return s.split(' ').map(word => {
    let sortedWord = '';
    for (let char of word) {
      sortedWord += char.toLowerCase().charCodeAt(0) < 127 ? char : '';
    }
    return sortedWord;
  }).join(' ');
};
```

Explanation:

1. First, we split the input string into an array of words using the `split()` method with a space character as the separator.
2. Then, we use the `map()` method to transform each word into a new word where all characters are in ascending order based on ASCII value.
3. Inside the `map()` callback function, we use a `for...of` loop to iterate over each character in the word.
4. We use the `charCodeAt()` method to get the ASCII value of each character, and the `toLowerCase()` method to ensure the comparison is case-insensitive.
5. We then check if the ASCII value is less than 127 (the ASCII value for the first non-ASCII character, which is 128 for most languages). If it is, we add the character to the `sortedWord` string. If not, we skip it.
6. Finally, we use the `join()` method to concatenate the sorted words back into a single string, with spaces in between.

Note: The `charCodeAt(0)` method returns the ASCII value of the character at the specified position (in this case, the first character of the word). The `toLowerCase()` method is used to ensure the comparison is case-insensitive. The condition `charCodeAt(0) < 127` is used to skip non-ASCII characters, which are typically used in languages other than English. If you want to include non-ASCII characters, you can remove this condition.