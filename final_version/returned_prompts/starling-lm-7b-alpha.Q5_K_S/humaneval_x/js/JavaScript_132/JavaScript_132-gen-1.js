  let count = 0;
  for (const c of string) {
    if (c == '[') {
      count += 1;
    } else if (c == ']') {
      count -= 1;
      if (count < 0) {
        return true;
      }
    }
  }
  return count > 0;
}



