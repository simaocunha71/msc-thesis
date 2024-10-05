Here is a JavaScript function that meets the requirements:
```
const fileNameCheck = (file_name) => {
  const regex = /^[a-zA-Z][a-zA-Z0-9\.]{0,10}(?:txt|exe|dll)$/i;
  return regex.test(file_name) ? 'Yes' : 'No';
};
```
Here's an explanation of the regular expression used:

* `^` matches the start of the string
* `[a-zA-Z]` matches a single letter (either uppercase or lowercase) at the start of the string
* `[a-zA-Z0-9\.]{0,10}` matches the remaining part of the string, allowing up to 10 characters (including letters, digits, and dot)
* `(?:txt|exe|dll)` is a non-capturing group that matches one of the allowed extensions (txt, exe, or dll)
* `$` matches the end of the string
* `i` at the end makes the pattern case-insensitive

The function uses the `test()` method to check if the regular expression matches the file name. If it does, the function returns 'Yes', otherwise it returns 'No'.