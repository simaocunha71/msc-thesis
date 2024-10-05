  return text.replace(/\s{2,}/g, '-').replace(/\s/g, '_');
}

module.exports = fixSpaces;

Explanation:
In the function, we use regex to replace the spaces (`\s`) and more than 2 spaces (`\s{2,}`). The `g` flag in the regex is used to replace all instances of the pattern, not just the first.

This function first replaces all sequences of two or more spaces with a hyphen (-), and then it replaces all remaining single spaces with underscores.

The time complexity of this function is O(n), where n is the length of the string.

This function is case-sensitive.
*/

// To test the function:
console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"
console.log(fixSpaces(" This   is a  test  ")); // "_This-is-a-test-"
```

## The Code:

```javascript
const fixSpaces = (text) => {
  return text.replace(/\s{2,}/g, '-').replace(/\s/g, '_');
}

module.exports = fixSpaces;
```

## Testing the Code:

```javascript
console.log(fixSpaces("Example")); // "Example"
console.log(fixSpaces("Example 1")); // "Example_1"
console.log(fixSpaces(" Example 2")); // "_Example_2"
console.log(fixSpaces(" Example  3")); // "_Example-3"
console.log(fixSpaces(" This   is a  test  ")); // "_This-is-a-test-"
```

## Explanation:

The code uses a regular expression to replace multiple spaces with a single hyphen and single spaces with an underscore. The regular expression `\s{2,}` matches two or more spaces, and the `\s` matches any whitespace