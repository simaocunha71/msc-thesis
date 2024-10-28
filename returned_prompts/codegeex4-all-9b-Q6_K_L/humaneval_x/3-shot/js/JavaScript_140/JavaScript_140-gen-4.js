  var result = "";
  var count = 0;
  for (const c of text) {
    if (c == ' ') {
      count += 1;
    } else {
      if (count > 2) {
        result += '-';
      } else if (count > 0) {
        result += '_';
      }
      result += c;
      count = 0;
    }
  }

  if (count > 2) {
    result += '-';
  } else if (count > 0) {
    result += '_';
  }

  return result;
}