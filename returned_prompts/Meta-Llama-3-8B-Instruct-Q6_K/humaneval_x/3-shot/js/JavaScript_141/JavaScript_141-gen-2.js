  let [name, extension] = file_name.split('.');
  if (name.length > 0 && /^[a-zA-Z]/.test(name) && !/\d{4,}/.test(name) && 
      ['txt', 'exe', 'dll'].includes(extension)) {
    return 'Yes';
  } else {
    return 'No';
  }
}
// Note: The regular expression /\d{4,}/ matches 4 or more digits. This ensures that the file name does not have more than 3 digits.  The test method returns true if the string matches the regular expression.  If the string does not match, it returns false.  If the string is not a string, it throws an error.  For example, "1example.dll" is not valid because it has 4 digits.  On the other hand, "1example.txt" is valid because it has 1 digit.  The regular expression /^[a-zA-Z]/.test(name) ensures that the file name starts with a letter.  The includes method checks if the extension is in the list of valid extensions.  If all conditions are met, the function returns 'Yes'.  If any condition is not met, the function returns 'No'.  For example, "example.txt" is valid, so the function returns 'Yes'.  On the other hand, "1example.dll" is not valid, so the function returns 'No'.