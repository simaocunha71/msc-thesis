  if (strings.length == 0) {
    return null;
  }

  var longest_string = strings[0];
  var longest_length = strings[0].length;

  for (const s of strings) {
    if (s.length > longest_length) {
      longest_length = s.length;
      longest_string = s;
    }
  }

  return longest_string;
}



