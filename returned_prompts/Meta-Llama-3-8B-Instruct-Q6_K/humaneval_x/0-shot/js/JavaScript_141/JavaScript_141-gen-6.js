```javascript
const fileNameCheck = (file_name) => {
  if (/\d{4,}/.test(file_name)) return 'No'; // Check if there are more than three digits
  if (file_name.indexOf('.') !== -1) { // Check if there is exactly one dot
    const [name, extension] = file_name.split('.');
    if (!/[a-zA-Z]/.test(name.charAt(0))) return 'No'; // Check if the name starts with a letter
    if (!['txt', 'exe', 'dll'].includes(extension)) return 'No'; // Check the extension
  } else return 'No'; // If there is no dot, the file's name is not valid
  return 'Yes'; // If all conditions are met, the file's name is valid
};
```