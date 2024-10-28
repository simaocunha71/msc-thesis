  if (strings.length == 0) {
    return null;
  }
  var longest_string = strings[0];
  for (const str of strings) {
    if (str.length > longest_string.length) {
      longest_string = str;
    }
  }
  return longest_string;
}