  if (/^[a-zA-Z]+[a-zA-Z0-9]*\.[a-zA-Z]{3}(?:$|\.)/.test(file_name)) {
    return 'Yes';
  } else {
    return 'No';
  }
}
// Explanation:
// The regular expression checks the following:
// - The file name starts with one or more latin letters or digits.
// - The file name contains exactly one dot.
// - The substring after the dot is exactly 3 letters (one of ['txt', 'exe', 'dll']).
// If the file name matches the regular expression, the function returns 'Yes', otherwise 'No'.