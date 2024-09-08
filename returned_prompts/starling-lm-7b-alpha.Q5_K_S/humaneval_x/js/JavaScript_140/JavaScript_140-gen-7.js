  let result = '';
  let count = 0;

  for (const c of text) {
    if (c == ' ') {
      if (count == 0) {
        result += '_';
      } else {
        result += '-';
        count = 0;
      }
    } else {
      result += c;
      count = 0;
    }
  }
  return result;
}



