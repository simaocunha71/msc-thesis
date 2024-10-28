  var open_brackets = 0;

  for (const c of string) {
    if (c == '[') {
      open_brackets += 1;
    } else if (c == ']') {
      open_brackets -= 1;
    }
  }

  return open_brackets > 0;
}



