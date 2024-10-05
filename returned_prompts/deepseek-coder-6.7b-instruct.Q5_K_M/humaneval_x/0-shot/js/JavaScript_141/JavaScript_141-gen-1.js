  const nameParts = file_name.split('.');
  const name = nameParts[0];
  const extension = nameParts[1];

  // Check that there is exactly one dot in the file name and that the name and extension aren't empty
  if (nameParts.length !== 2 || !name || !extension) {
    return 'No';
  }

  // Check that there are no more than 3 digits in the name
  const nameDigits = name.match(/\d/g);
  if (nameDigits && nameDigits.length > 3) {
    return 'No';
  }

  // Check that the name starts with a letter
  if (!/[a-zA-Z]/.test(name.charAt(0))) {
    return 'No';
  }

  // Check that the extension is one of the allowed ones
  if (!['txt', 'exe', 'dll'].includes(extension)) {
    return 'No';
  }

  return 'Yes';
}

console.log(fileNameCheck("example.txt")); // Yes
console.log(fileNameCheck("1example.dll")); // No
console.log(fileNameCheck("example1.txt")); // Yes
console.log(fileNameCheck("example.exe")); // Yes
console.log(fileNameCheck("example1.dll")); // Yes
console.log(fileNameCheck("example.1txt")); // No
console.log(fileNameCheck("example.dll1")); // No
console.log(fileNameCheck(".txt")); // No
console.log(fileNameCheck("example")); // No
console.log(fileNameCheck("example.")); // No
console.log(fileNameCheck("example.dll")); // Yes
console.log(fileNameCheck("example123.txt")); // No
console.log(fileNameCheck("ex123ample.txt")); // No
console.log(fileNameCheck("ex@mple.txt")); // No
console.log(fileNameCheck("example.doc")); // No
console.log(fileNameCheck("example.dll.txt")); // No
console.log(fileNameCheck