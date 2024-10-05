Here is a JavaScript function that meets the requirements:
```
const fileNameCheck = (file_name) => {
  const regex = /^[a-zA-Z][a-zA-Z0-9]*(?:\.[a-zA-Z]{3}(?:txt|exe|dll))$/;
  return regex.test(file_name) ? 'Yes' : 'No';
};
```
Here's a breakdown of the regular expression used:

* `^` matches the start of the string
* `[a-zA-Z]` matches a letter (either uppercase or lowercase) that starts the string
* `[a-zA-Z0-9]*` matches zero or more letters or digits
* `(?:\.[a-zA-Z]{3}(?:txt|exe|dll))` is a non-capturing group that matches the following:
	+ `\.` matches a dot
	+ `[a-zA-Z]{3}` matches exactly three letters (either uppercase or lowercase)
	+ `(?:txt|exe|dll)` matches one of the allowed extensions (txt, exe, or dll)
* `$` matches the end of the string

The `test()` method checks if the regular expression matches the input string. If it does, the function returns 'Yes', otherwise it returns 'No'.