  if (strings.length == 0) {
    return null;
  }

  var longest_string = strings[0];
  for (const s of strings) {
    if (s.length > longest_string.length) {
      longest_string = s;
    }
  }
  return longest_string;
}



