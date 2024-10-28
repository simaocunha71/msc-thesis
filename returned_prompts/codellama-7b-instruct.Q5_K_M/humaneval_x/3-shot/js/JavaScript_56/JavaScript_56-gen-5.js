  var open_bracket_count = 0;
  for (const c of brackets) {
    if (c == '<') {
      open_bracket_count += 1;
    } else if (c == '>') {
      open_bracket_count -= 1;
    }
  }
  return open_bracket_count == 0;
}



