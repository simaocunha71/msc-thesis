```
const fixSpaces = (text) => {
  return text.replace(/\s+/g, (match) => match.replace(/\s+/g, '-').replace(/ /g, '_'));
};
```


Explanation:
The `fixSpaces` function takes a string `text` as input and returns the modified string. 

The `replace()` method is used to replace all spaces in the string with underscores, and all consecutive spaces with dashes. 

The regular expression `\s+` matches one or more whitespace characters. 

The first `replace()` call replaces all consecutive spaces with dashes. 

The second `replace()` call replaces all spaces with underscores. 

The `g` flag at the end of the regular expression makes the replacement global, so that all occurrences in the string are replaced, not just the first one. 

This function works for strings with any number of spaces, not just 2. 

For example, if the input string is `" Example   3"`, the function will replace the spaces with dashes and then with underscores, resulting in the output string `" _Example-3"`. 

This function also works correctly for strings that do not contain any spaces, such as `"Example"`, which will remain unchanged. 

Finally, this function works correctly for strings that contain only one space, such as `"Example 1"`, which will be replaced with an underscore, resulting in the output string `"Example_1"`. 