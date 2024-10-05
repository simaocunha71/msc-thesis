```
const wordsString = (s) => s.split(/[,\s]/);
```


Explanation:
The `split()` method is used to split a string into an array of substrings. It takes a regular expression as an argument, which is used to match the separator(s) to split the string.

In this case, we're using a regular expression that matches both commas and spaces: `[,\s]`. The square brackets `[]` are used to create a character class, which matches any character within the class. The `,` and `\s` are individual characters that are matched.

By default, the `split()` method splits the string at each occurrence of the separator(s) and returns an array of the resulting substrings. So, when we pass `[,\s]` as the argument, it splits the string at each comma or space, effectively converting the string of words into an array of words.