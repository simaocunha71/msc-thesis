  let result = '';
  let consecutive_spaces = 0;

  for (const c of text) {
    if (c == ' ') {
      if (consecutive_spaces == 0) {
        result += '_';
      } else if (consecutive_spaces == 1) {
        result += '-';
      }
      consecutive_spaces += 1;
    } else {
      result += c;
      consecutive_spaces = 0;
    }
  }

  return result;
}



