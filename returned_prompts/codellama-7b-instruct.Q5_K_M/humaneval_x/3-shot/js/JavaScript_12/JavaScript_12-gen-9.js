  if (strings.length == 0) {
    return null;
  }
  let longest_string = strings[0];
  let longest_length = longest_string.length;
  for (const s of strings) {
    if (s.length > longest_length) {
      longest_length = s.length;
      longest_string = s;
    }
  }
  return longest_string;
}



