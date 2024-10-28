  if (strings.length == 0) {
    return null;
  }
  var longest_str = strings[0];
  for (const str of strings) {
    if (str.length > longest_str.length) {
      longest_str = str;
    }
  }
  return longest_str;
}