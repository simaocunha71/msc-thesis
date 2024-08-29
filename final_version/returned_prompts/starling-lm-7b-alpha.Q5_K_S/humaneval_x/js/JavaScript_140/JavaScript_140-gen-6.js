  let result = '';
  let spaces = 0;
  for (const c of text) {
    if (c == ' ') {
      spaces += 1;
    } else {
      if (spaces > 2) {
        result += '-';
        spaces = 2;
      } else {
        result += '_';
        spaces = 0;
      }
      result += c;
    }
  }

  return result;
}



