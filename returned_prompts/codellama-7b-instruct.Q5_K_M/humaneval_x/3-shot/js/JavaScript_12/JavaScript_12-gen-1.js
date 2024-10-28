  if (strings.length == 0) {
    return null;
  }

  var longest_string = strings[0];
  var longest_len = strings[0].length;

  for (const s of strings) {
    if (s.length > longest_len) {
      longest_len = s.length;
      longest_string = s;
    }
  }

  return longest_string;
}



