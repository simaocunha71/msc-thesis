```
const fixSpaces = (text) => {
  return text.replace(/ +/g, (match) => {
    if (match.length > 2) {
      return '-';
    } else {
      return '_';
    }
  });
};
```



This function uses the `replace()` method to replace all spaces in the `text` string with either an underscore or a hyphen, depending on whether the space is part of a sequence of 2 or more consecutive spaces.

Here's a breakdown of the regular expression used in the `replace()` method:

* ` +`: matches one or more spaces
* `g`: global flag, which makes the replacement apply to all occurrences in the string, not just the first one

The callback function passed to `replace()` is called for each match. It checks the length of the match (i.e., the number of consecutive spaces) and returns either an underscore or a hyphen accordingly.

For example, if the input string is `" Example   3"`, the `replace()` method will call the callback function twice:

1. First, it matches the sequence `" "`, which has a length of 1. The callback function returns an underscore `_`.
2. Then, it matches the sequence `"   "`, which has a length of 3. The callback function returns a hyphen `-`.

The resulting string is `" _Example-3"`, which is the desired output.