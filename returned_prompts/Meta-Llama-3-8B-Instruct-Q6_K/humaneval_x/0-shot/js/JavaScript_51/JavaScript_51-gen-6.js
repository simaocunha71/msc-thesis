Here is a possible solution using a regular expression:
```
const removeVowels = (text) => {
  return text.replace(/[aeiouAEIOU]/g, '');
};
```
This function uses the `replace()` method to replace all occurrences of vowels (both lowercase and uppercase) with an empty string (`''`). The regular expression `/[aeiouAEIOU]/g` matches any vowel character (either lowercase or uppercase). The `g` flag at the end of the regular expression makes the replacement global, so that all occurrences are replaced, not just the first one.

For example, if you call `removeVowels("abcdef\nghijklm")`, the function will return `"bcdf\nghjklm"`, which is the original string with all vowels removed. If you call `removeVowels('aaaaa')`, the function will return `''`, since all characters are vowels and are replaced with an empty string. If you call `removeVowels('aaBAA')`, the function will return `'B'`, since only the vowels are replaced with an empty string, leaving the letter `'B'` intact. If you call `removeVowels('zbcd')`, the function will return `'zbcd'`, since there are no vowels to replace.