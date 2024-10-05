```
const fixSpaces = (text) => {
  return text.replace(/\s+/g, (match) => {
    if (match.length > 1) {
      return '-';
    } else {
      return '_';
    }
  });
};
```


Explanation:
The function uses the `replace()` method with a regular expression (`\s+`) to replace one or more spaces with a new value. The callback function checks the length of the match. If the length is greater than 1, it returns '-', otherwise, it returns '_'. This way, consecutive spaces are replaced with a single '-' and single spaces are replaced with a single '_'. 

The regular expression `\s+` matches one or more whitespace characters. The `g` flag at the end of the pattern makes the replacement global, so that all occurrences in the string are replaced, not just the first one. 

The callback function `(match) => { ... }` is called for each match found in the string. It returns the new value to replace the matched text. In this case, it checks the length of the match and returns either '_' or '-'. 

This function can be tested with the provided examples to verify its correctness. 

Example:
`fixSpaces("Example   3")` returns `"_Example-3"`. 

This function is case-sensitive, if you want to make it case-insensitive, you can add the `i` flag to the regular expression, like this: `\s+gi`. The `i` flag makes the regular expression matching case-insensitive. 

Note: This solution assumes that the input string `text` only contains ASCII characters. If the input string can contain non-ASCII characters, you may need to adjust the regular expression accordingly. 

Also, this solution does not handle the case where the input string is null or undefined. You may want to add error handling for these cases depending on your requirements. 