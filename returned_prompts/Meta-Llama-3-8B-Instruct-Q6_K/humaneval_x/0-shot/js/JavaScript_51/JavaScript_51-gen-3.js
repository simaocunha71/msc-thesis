```
const removeVowels = (text) => {
  return text.replace(/[aeiouAEIOU]/g, '');
};
```
This function uses the `replace()` method with a regular expression to remove all vowels from the input string. The regular expression `/[aeiouAEIOU]/g` matches any vowel (both lowercase and uppercase) and the `g` flag at the end makes it match all occurrences in the string, not just the first one. The `replace()` method then replaces all matches with an empty string, effectively removing them from the string. The resulting string without vowels is then returned.