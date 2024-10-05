```
const removeVowels = (text) => {
  return text.replace(/[aeiouAEIOU]/g, '');
};
```


Explanation:
The provided solution uses the `replace()` method of the string to remove all vowels from the input text. The regular expression `/[aeiouAEIOU]/g` matches any vowel (both lowercase and uppercase) in the text. The `g` flag at the end of the regular expression makes it match all occurrences in the text, not just the first one. The `replace()` method replaces each match with an empty string, effectively removing the vowels from the text. The resulting string is then returned by the `removeVowels` function.