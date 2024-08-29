  let result = '';
  let previous_space = true;
  let consecutive_spaces = 0;

  for (const c of text) {
    if (c == ' ') {
      if (previous_space) {
        consecutive_spaces += 1;
      } else {
        if (consecutive_spaces >= 2) {
          result += '-';
        } else {
          result += '_';
        }
        consecutive_spaces = 1;
      }
      previous_space = true;
    } else {
      result += c;
      previous_space = false;
    }
  }

  if (previous_space && consecutive_spaces >= 2) {
    result += '-';
  } else {
    result += '_';
  }

  return result;
}



