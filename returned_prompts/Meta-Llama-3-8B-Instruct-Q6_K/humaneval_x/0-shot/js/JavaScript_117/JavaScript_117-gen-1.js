```javascript
const selectWords = (s, n) => {
  const words = s.split(' ');
  const result = [];

  for (let word of words) {
    const consonantCount = word.replace(/[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]/g, '').length;
    if (consonantCount === n) {
      result.push(word);
    }
  }

  return result;
};
```
Explanation:
The `selectWords` function takes two parameters: `s` (the input string) and `n` (the number of consonants to look for). It first splits the input string into an array of words using the `split` method with a space character as the separator.

Then, it iterates over each word in the array. For each word, it counts the number of consonants using a regular expression. The regular expression `/[^bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]/g` matches any character that is not a consonant (i.e., a vowel or a space). The `replace` method is used to replace all non-consonant characters with an empty string, and the `length` property is used to get the length of the resulting string, which is the number of consonants in the word.

If the number of consonants in a word is equal to `n`, the word is added to the `result` array.

Finally, the `result` array is returned as the result of the function.

Note that this implementation assumes that the input string only contains letters and spaces. If the input string can contain other characters, additional error handling may be necessary.