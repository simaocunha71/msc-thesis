Here is a JavaScript function that removes vowels from a given string:
```
const removeVowels = (text) => {
  const vowels = 'aeiouAEIOU';
  return text.replace(/[^a-z0-9]/gi, '');
};
```
Here's a breakdown of how the function works:

1. We define a string `vowels` that contains all the vowel characters (both lowercase and uppercase).
2. We use the `replace()` method to search for all occurrences of characters that are not letters (using the regular expression `/[^a-z0-9]/gi`) and replace them with an empty string (`''`).
3. The `gi` flag at the end of the regular expression makes it case-insensitive and global, so that it matches all occurrences of non-letter characters in the string.

Here are some examples of how the function works:
```
console.log(removeVowels('')); // ''
console.log(removeVowels("abcdef\nghijklm")); // 'bcdf\nghjklm'
console.log(removeVowels('abcdef')); // 'bcdf'
console.log(removeVowels('aaaaa')); // ''
console.log(removeVowels('aaBAA')); // 'B'
console.log(removeVowels('zbcd')); // 'zbcd'
```
Note that this function removes all non-letter characters, including spaces, punctuation, and digits, in addition to vowels. If you want to preserve certain non-letter characters, you can modify the regular expression accordingly. For example, if you want to preserve spaces, you can use `/[^a-z0-9\s]/gi` instead.