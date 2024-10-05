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



The `fixSpaces` function takes a string `text` as input and returns a new string where all spaces are replaced with either underscores or hyphens.

Here's how it works:

1. The `replace` method is called on the input `text` with a regular expression `/ +/g`. This regular expression matches one or more spaces (`+`) in the string, and the `g` flag makes it global, so that all occurrences are replaced.
2. The replacement function is called for each match. This function checks the length of the match (`match.length`) and returns either an underscore (`_`) if the length is 1, or a hyphen (`-`) if the length is greater than 1.

Here are some test cases to demonstrate the function's behavior:

```
console.log(fixSpaces("Example")); // Output: "Example"
console.log(fixSpaces("Example 1")); // Output: "Example_1"
console.log(fixSpaces(" Example 2")); // Output: "_Example_2"
console.log(fixSpaces(" Example   3")); // Output: "_Example-3"
```

I hope this helps! Let me know if you have any further questions. 😊

Explanation:

The regular expression `/ +/g` matches one or more spaces (`+`) in the string, and the `g` flag makes it global, so that all occurrences are replaced.

The replacement function is called for each match, and it returns either an underscore (`_`) if the length of the match is 1, or a hyphen (`-`) if the length is greater than 1.

This is because the problem statement asks to replace all spaces with underscores, and if a string has more than 2 consecutive spaces, then replace all consecutive spaces with a hyphen.

The `match.length` property returns the length of the matched string, which is the number of consecutive spaces. If the length is 1, it means there is only one space, so we replace it with an underscore. If the length is greater than 1, it means there are more than one consecutive spaces, so we replace them with a hyphen.

This solution is efficient because it uses a regular expression to match multiple spaces at once