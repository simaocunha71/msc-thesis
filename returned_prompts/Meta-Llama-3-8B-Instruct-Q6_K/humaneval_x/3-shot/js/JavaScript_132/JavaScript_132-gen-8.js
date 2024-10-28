  let depth = 0;
  for (const c of string) {
    if (c == '[') {
      depth++;
    } else if (c == ']') {
      if (depth > 0) {
        depth--;
      } else {
        return false;
      }
    }
  }
  return depth > 0;
}