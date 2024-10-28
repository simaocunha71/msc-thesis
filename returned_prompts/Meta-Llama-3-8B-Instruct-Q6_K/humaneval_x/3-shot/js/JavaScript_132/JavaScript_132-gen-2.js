  let count = 0;
  for (const c of string) {
    if (c == '[') {
      count++;
    } else if (c == ']') {
      if (count > 0) {
        count--;
      } else {
        return false;
      }
    }
  }
  return count > 0;
}