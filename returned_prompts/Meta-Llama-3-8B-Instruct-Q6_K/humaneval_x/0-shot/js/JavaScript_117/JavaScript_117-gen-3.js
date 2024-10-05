Here is the solution in JavaScript:
```
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];
  let consonantCount = 0;

  for (const word of words) {
    for (const char of word) {
      if (!['a', 'e', 'i', 'o', 'u'].includes(char.toLowerCase())) {
        consonantCount++;
      }
    }
    if (consonantCount === n) {
      result.push(word);
    }
    consonantCount = 0;
  }

  return result;
};
```
Here's an explanation of the solution:

1. We split the input string `s` into an array of words using the `split` method.
2. We initialize an empty array `result` to store the words that contain exactly `n` consonants.
3. We initialize a variable `consonantCount` to keep track of the number of consonants in each word.
4. We iterate over each word in the `words` array.
5. For each word, we iterate over each character in the word.
6. If the character is not a vowel (i.e., it's a consonant), we increment `consonantCount`.
7. If `consonantCount` is equal to `n`, we add the word to the `result` array.
8. We reset `consonantCount` to 0 for the next word.
9. Finally, we return the `result` array.

Note that this solution assumes that the input string contains only letters and spaces, as stated in the problem description. If the input string can contain other characters, you may need to modify the solution accordingly.