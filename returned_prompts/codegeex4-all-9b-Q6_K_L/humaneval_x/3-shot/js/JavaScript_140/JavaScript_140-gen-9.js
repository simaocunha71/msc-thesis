  var result = "";
  var consecutive_spaces = 0;

  for (const c of text) {
    if (c == ' ') {
      consecutive_spaces += 1;
      if (consecutive_spaces > 2) {
        result += '-';
      } else {
        result += '_';
      }
    } else {
      consecutive_spaces = 0;
      result += c;
    }
  }

  return result;
}