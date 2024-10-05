Here is a JavaScript function that checks the validity of a file name according to the given conditions. It uses regular expressions to match the conditions.

```javascript
const fileNameCheck = (file_name) => {
  const regex = /^[a-zA-Z][a-zA-Z0-9]{0,38}\.[txt|exe|dll]$/;
  return regex.test(file_name) ? 'Yes' : 'No';
};
```

This function uses the following regular expression:
- `^[a-zA-Z]` matches the start of the string and ensures that it starts with a letter from the latin alphabet.
- `[a-zA-Z0-9]{0,38}` matches 0 to 38 occurrences of a letter from the latin alphabet or a digit.
- `\.` matches a dot.
- `[txt|exe|dll]$` matches the end of the string and ensures that it ends with 'txt', 'exe', or 'dll'.

The `test()` method of the regular expression is used to test the file name against the regular expression. If the file name matches the regular expression, the function returns 'Yes', otherwise it returns 'No'.