```javascript
const fileNameCheck = (file_name) => {
  const regex = /^[a-zA-Z][a-zA-Z0-9]*(?:\.[a-z]{3,4})?$/;
  return regex.test(file_name) ? 'Yes' : 'No';
};
```
The function `fileNameCheck` takes a string as an argument and checks if the file name is valid according to the given conditions. 

The regular expression `/^[a-zA-Z][a-zA-Z0-9]*(?:\.[a-z]{3,4})?$/` is used to match the file name. Here's a breakdown of the regular expression:
- `^` matches the start of the string.
- `[a-zA-Z]` matches a letter (either uppercase or lowercase) at the start of the string.
- `[a-zA-Z0-9]*` matches zero or more alphanumeric characters after the letter.
- `(?:\.[a-z]{3,4})?` is a non-capturing group that matches a dot followed by 3 to 4 lowercase letters. The `?` after the group makes it optional.
- `$` matches the end of the string.

The `test()` method is used to test the file name against the regular expression. If the file name matches the regular expression, the function returns `'Yes'`, otherwise it returns `'No'`. 

This function can be used to check if a file name is valid according to the given conditions. For example, `fileNameCheck("example.txt")` returns `'Yes'`, and `fileNameCheck("1example.dll")` returns `'No'`. 