  return text.replace(/\s{2,}/g, "-").replace(/ /g, "_");

};

// Test cases
console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"
```

This solution uses JavaScript's built-in `replace()` method with a regular expression to replace spaces with underscores and multiple consecutive spaces with a single hyphen.

The regular expression `\s{2,}` matches any sequence of 2 or more whitespace characters (including spaces, tabs, etc.), while `\s` matches any whitespace character.

The `g` flag at the end of the regular expression tells `replace()` to replace all occurrences, not just the first one.

Finally, the `replace()` method is called twice: first to replace all single spaces with underscores, and second to replace all multiple consecutive spaces with a single hyphen.

This solution assumes that the input text does not contain any non-whitespace characters. If this is not the case, you might need to adjust the regular expressions to match only spaces.

Also, if you want to replace all types of spaces (not just regular spaces, but also tabs and newlines) with underscores, you can use the `\s` regular expression.

```javascript
const fixSpaces = (text) => {
  return text.replace(/\s+/g, "_");
};
```
This solution will replace all types of spaces with underscores.
*/

const fixSpaces = (text) => {
  return text.replace(/\s{2,}/g, "-").replace(/ /g, "_");
};

// Test cases
console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"

```

This solution uses JavaScript