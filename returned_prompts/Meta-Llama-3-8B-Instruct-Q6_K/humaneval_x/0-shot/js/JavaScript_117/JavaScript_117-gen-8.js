Here is a possible implementation of the `selectWords` function in JavaScript:
```javascript
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];

  for (const word of words) {
    let consonantCount = 0;
    for (const char of word) {
      if (!['a', 'e', 'i', 'o', 'u'].includes(char.toLowerCase())) {
        consonantCount++;
      }
    }
    if (consonantCount === n) {
      result.push(word);
    }
  }
  return result;
};
```
Here's an explanation of how the function works:

1. We split the input string `s` into an array of words using the `split` method with a space character as the separator.
2. We initialize an empty array `result` that will store the words that contain exactly `n` consonants.
3. We loop through each word in the `words` array.
4. For each word, we count the number of consonants using a nested loop that iterates through each character of the word. We use the `includes` method to check if the character is not one of the vowels (a, e, i, o, u). If it's not a vowel, we increment the `consonantCount` variable.
5. If the `consonantCount` is equal to `n`, we add the word to the `result` array.
6. Finally, we return the `result` array.

You can test the function with the examples provided in the problem statement to verify that it works correctly. For example:
```javascript
console.log(selectWords("Mary had a little lamb", 4)); // Output: ["little"]
console.log(selectWords("Mary had a little lamb", 3)); // Output: ["Mary"]
console.log(selectWords("simple white space", 2)); // Output: []
console.log(selectWords("Hello world", 4)); // Output: ["world"]
console.log(selectWords("Uncle sam", 3)); // Output: ["Uncle"]
``` I hope this helps! Let me know if you have any questions. 😊

**Note:** This implementation assumes that the input string only contains letters and spaces. If the input string can contain other characters, you may need to modify the implementation accordingly. For example, you could use a regular expression to match only letters and spaces, and then split the string on that pattern