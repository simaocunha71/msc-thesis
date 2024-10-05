  var depth = 0;
  for (const c of string) {
    if (c == '[') {
      depth += 1;
    } else {
      depth -= 1;
    }
    if (depth < 0) {
      return false;
    }
  }
  if (depth == 0) {
    return false;
  }
  return true;
}



