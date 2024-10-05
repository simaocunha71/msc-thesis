```
const removeVowels = (text) => text.replace(/[aeiou]/gi, '');
```


Explanation:
The function `removeVowels` takes a string `text` as input and returns a new string with all vowels removed. 

The `replace` method is used with a regular expression to replace all occurrences of vowels with an empty string (`''`). The regular expression `/[aeiou]/gi` matches any character that is a vowel (both lowercase and uppercase) and the `g` flag at the end makes it global, so all occurrences are replaced, not just the first one. The `i` flag makes the match case-insensitive.

For example, if the input string is "abcdef", the function will return "bcdf". If the input string is "aaaaa", the function will return an empty string. If the input string is "aaBAA", the function will return "B". If the input string is "zbcd", the function will return "zbcd". 