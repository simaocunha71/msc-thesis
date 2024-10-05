  let depth = 0;
  for (const c of string) {
    if (c == '[') {
      depth += 1;
    } else if (c == ']') {
      depth -= 1;
    }
    if (depth < 0) {
      return true;
    }
  }
  if (depth > 0) {
    return true;
  }
  return false;
}