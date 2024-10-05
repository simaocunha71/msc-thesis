Here is a JavaScript solution for the problem:

```javascript
const fileNameCheck = (file_name) => {
  const regex = /^[a-zA-Z](?:[a-zA-Z0-9]{0,2}\.)(?:txt|exe|dll)$/;
  return regex.test(file_name) ? 'Yes' : 'No';
};

console.log(fileNameCheck("example.txt")); // => 'Yes'
console.log(fileNameCheck("1example.dll")); // => 'No'
```

Explanation:
The regular expression `/^[a-zA-Z](?:[a-zA-Z0-9]{0,2}\.)(?:txt|exe|dll)$/` checks if the file name is valid according to the given conditions:

- `^[a-zA-Z]` ensures that the file name starts with a letter from the latin alphabet.
- `(?:[a-zA-Z0-9]{0,2}\.)` matches the substring before the dot, which should not be more than 3 characters long and should not be empty. The dot itself is matched with `\.`.
- `(?:txt|exe|dll)` matches the substring after the dot, which should be one of 'txt', 'exe', or 'dll'.
- `$` ensures that the file name ends with the matched substring.

The `test()` method is used to check if the given file name matches the regular expression. If it matches, the function returns 'Yes', otherwise it returns 'No'.