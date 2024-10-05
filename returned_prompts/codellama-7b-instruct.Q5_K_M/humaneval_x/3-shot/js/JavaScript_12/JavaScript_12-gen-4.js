  if (strings.length == 0) return null;

  var longest_string = strings[0];
  var longest_length = strings[0].length;

  for (const s of strings) {
    if (s.length > longest_length) {
      longest_string = s;
      longest_length = s.length;
    }
  }

  return longest_string;
}



