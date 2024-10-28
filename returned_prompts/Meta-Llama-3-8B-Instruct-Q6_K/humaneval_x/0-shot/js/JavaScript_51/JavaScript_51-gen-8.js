```
const removeVowels = (text) => {
  return text.replace(/[aeiouAEIOU]/g, '');
};
```

Explanation:
The `replace()` method is used to replace all vowels (both lowercase and uppercase) in the input `text` with an empty string, effectively removing them. The regular expression `/[aeiouAEIOU]/g` matches any vowel (both lowercase and uppercase), and the `g` flag at the end ensures that all matches are replaced, not just the first one.

For example, if the input is `'abcdef'`, the regular expression would match the vowels `'a'`, `'e'`, and `'e'`, and replace them with an empty string, resulting in the output `'bcd'`. Similarly, if the input is `'aaBAA'`, the regular expression would match the vowels `'a'` and `'a'`, and replace them with an empty string, resulting in the output `'B'`. If the input is `'zbcd'`, the regular expression would not match any vowels, so the output would be the same as the input. If the input is `'aaaaa'`, the regular expression would match all vowels and replace them with an empty string, resulting in an empty string as the output.