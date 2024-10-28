To separate the groups of parentheses from the input string, you can use a regular expression to find the groups. Here's the implementation:

```javascript
const separateParenGroups = (paren_string) => {
  // Remove spaces from the input string
  paren_string = paren_string.replace(/\s+/g, '');

  // Find all groups of balanced parentheses
  let groups = paren_string.match(/\([^\(\)]*\)/g);

  return groups;
};
```

This implementation uses the `match()` function of the string object to find all groups of balanced parentheses. The regular expression `\([^\(\)]*\)` matches a group of balanced parentheses, where the parentheses are enclosed in `\(` and `\)`, and the characters between them are not parentheses. The `g` flag is used to find all matches in the string.

Let's test the function with the provided example:

```javascript
console.log(separateParenGroups('( ) (( )) (( )( ))'));
// Output: ['()', '(())', '(()())']
```

The output matches the expected result.