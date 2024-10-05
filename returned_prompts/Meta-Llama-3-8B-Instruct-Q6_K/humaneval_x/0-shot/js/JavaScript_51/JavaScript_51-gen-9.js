```
const removeVowels = (text) => {
  return text.replace(/[aeiou]/gi, '');
};
```


Explanation:
The removeVowels function uses the replace() method to replace all occurrences of vowels (a, e, i, o, u) in the input string with an empty string. The regular expression /[aeiou]/gi matches any vowel (both lowercase and uppercase) and the g flag at the end of the pattern makes the replacement global (i.e., it replaces all occurrences, not just the first one). The i flag makes the match case-insensitive, so both lowercase and uppercase vowels are replaced. The return statement returns the modified string.