You can use regular expressions to solve this problem. Here is one possible solution:

```javascript
const fixSpaces = (text) => {
  // Replace all spaces with underscores
  let newText = text.replace(/\s/g, '_');
  
  // Replace all consecutive underscores with a single underscore
  newText = newText.replace(/_+/g, '_');
  
  // Replace all consecutive underscores with a single dash
  newText = newText.replace(/_+/g, '-');
  
  return newText;
};
```

Here's how this solution works:

1. The first `replace` function replaces all spaces in the input string with underscores. This is done using the regular expression `\s`, which matches any whitespace character.
2. The second `replace` function replaces all consecutive underscores with a single underscore. This is done using the regular expression `_+`, which matches one or more underscores.
3. The third `replace` function replaces all consecutive underscores with a single dash. This is done using the same regular expression `_+`.
4. The resulting string is returned.