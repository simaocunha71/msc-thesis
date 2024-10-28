```
const wordsString = (s) => s.trim().split(/[ ,]+/);
```


Explanation:

*   We use the `trim()` method to remove any leading or trailing whitespace from the input string.
*   We then use the `split()` method with a regular expression as the separator. The regular expression `[ ,]+` matches one or more occurrences of either a space (` `) or a comma (`,`).
*   The `split()` method returns an array of words, which we return as the result.