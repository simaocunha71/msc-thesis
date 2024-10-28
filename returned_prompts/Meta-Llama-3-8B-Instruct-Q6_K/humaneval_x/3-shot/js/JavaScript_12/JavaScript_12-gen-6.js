  if (strings.length === 0) {
    return null;
  }
  var max_length = 0;
  var longest_string = strings[0];

  for (const s of strings) {
    if (s.length > max_length) {
      max_length = s.length;
      longest_string = s;
    }
  }

  return longest_string;
}