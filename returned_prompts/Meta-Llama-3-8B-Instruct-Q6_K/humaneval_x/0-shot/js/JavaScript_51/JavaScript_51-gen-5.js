```
const removeVowels = (text) => {
  const vowels = 'aeiouAEIOU';
  return text.replace(/[aeiouAEIOU]/g, '');
};
```


This function uses a regular expression to replace all occurrences of vowels in the input string with an empty string, effectively removing them. The `/[aeiouAEIOU]/g` pattern matches any vowel (both lowercase and uppercase) and the `g` flag at the end makes the replacement global, so all occurrences in the string are replaced. The `replace` method returns a new string with the replacements made.