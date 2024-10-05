Here is a JavaScript function that meets the requirements:

```javascript
const fileNameCheck = (file_name) => {
  if (file_name.length === 0) return 'No'; // file name is empty
  const parts = file_name.split('.');
  if (parts.length !== 2) return 'No'; // file name should contain exactly one dot
  if (!/^[a-zA-Z]/.test(parts[0])) return 'No'; // file name should start with a latin alphapet letter
  if (parts[1].length > 3 || /\D/.test(parts[1])) return 'No'; // file name should end with a valid extension
  const validExtensions = ['txt', 'exe', 'dll'];
  if (!validExtensions.includes(parts[1])) return 'No';
  return 'Yes';
};
```

This function first splits the file name into two parts at the dot. Then it checks if the file name is empty, if it contains exactly one dot, if the first part starts with a latin alphapet letter, and if the second part is a valid extension. If all conditions are met, the function returns 'Yes', otherwise it returns 'No'.