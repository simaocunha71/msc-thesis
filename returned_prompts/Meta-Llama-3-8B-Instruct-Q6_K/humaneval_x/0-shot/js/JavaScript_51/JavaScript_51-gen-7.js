```
const removeVowels = (text) => {
  const vowels = 'aeiouAEIOU';
  return text.replace(/[aeiouAEIOU]/g, '');
};
```



This function uses the `replace` method to replace all occurrences of vowels in the input string with an empty string. The regular expression `/[aeiouAEIOU]/g` matches any vowel character (both lowercase and uppercase) and the `g` flag at the end makes the replacement global, so that all occurrences in the string are replaced, not just the first one.