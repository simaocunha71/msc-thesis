  let nested = false;
  let opening = 0;
  for (const c of string) {
    if (c == '[') {
      opening++;
    } else if (c == ']') {
      if (opening > 0) {
        opening--;
      } else {
        return false;
      }
    }
    if (opening > 1) {
      nested = true;
      break;
    }
  }
  return nested;
}