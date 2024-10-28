  if (strings.length == 0) {
    return null;
  } else {
    var longest_string = strings[0];
    for (const string of strings) {
      if (string.length > longest_string.length) {
        longest_string = string;
      }
    }
    return longest_string;
  }
}



