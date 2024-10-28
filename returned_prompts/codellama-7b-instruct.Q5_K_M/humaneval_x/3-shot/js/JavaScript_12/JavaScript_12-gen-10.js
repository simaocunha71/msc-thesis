  if (strings.length == 0) {
    return null;
  }

  var longest_string = strings[0];
  var longest_length = longest_string.length;

  for (const string of strings) {
    if (string.length > longest_length) {
      longest_string = string;
      longest_length = string.length;
    }
  }

  return longest_string;
}



