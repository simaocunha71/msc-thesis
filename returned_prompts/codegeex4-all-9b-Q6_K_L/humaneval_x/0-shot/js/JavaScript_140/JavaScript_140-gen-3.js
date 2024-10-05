You can use the `replace` function with a regular expression to achieve this. Here's an example:

```javascript
const fixSpaces = (text) => {
  return text.replace(/\s+/g, function(match) {
    if (match.length > 2) {
      return "-";
    } else {
      return "_";
    }
  });
};
```

In this solution, the regular expression `\s+` matches one or more whitespace characters. The `g` flag makes it match all occurrences in the string. The `replace` function replaces each match with a new string, which is determined by the callback function. If the match has more than 2 characters, it returns "-", otherwise it returns "_".