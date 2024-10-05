The solution to this problem can be achieved by using a simple JavaScript function. Here is the code:

```javascript
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
The function `fixSpaces` takes a string `text` as an input and returns a new string with the spaces replaced according to the problem's requirements.

 Inside the `fixSpaces` function, the `replace` method of the string is used to replace all occurrences of one or more whitespace characters (`\s+`) with a new string.

The callback function passed to the `replace` method checks the length of the match (i.e., the consecutive spaces). If the length is greater than 1, it returns a hyphen (`-`); otherwise, it returns an underscore (`_`).

This way, if there are more than 2 consecutive spaces, they are replaced with a single hyphen, and all single spaces are replaced with an underscore. This meets the requirements of the problem.

For example, if the input is `" Example   3"`, the output will be `"_Example-3"`. If the input is `"Example 1"`, the output will be `"Example_1"`. If the input is `"Example"`, the output will be the same as the input.