  var open_brackets = 0;
  for (const c of brackets) {
    if (c == '<') {
      open_brackets += 1;
    } else if (c == '>') {
      open_brackets -= 1;
    }
    if (open_brackets < 0) {
      return false;
    }
  }
  return open_brackets == 0;
}



