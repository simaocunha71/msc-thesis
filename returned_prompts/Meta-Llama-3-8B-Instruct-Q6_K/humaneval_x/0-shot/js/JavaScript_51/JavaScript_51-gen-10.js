```
const removeVowels = (text) => {
  const vowels = 'aeiouAEIOU';
  return text.replace(new RegExp(`[${vowels}]`, 'g'), '');
};
```
This function uses the `replace` method with a regular expression to replace all vowels (both lowercase and uppercase) with an empty string, effectively removing them from the input string. The `g` flag at the end of the regular expression makes the replacement global, so that all occurrences of vowels are replaced, not just the first one. The function returns the resulting string without vowels.