  const chars = {};
  for (const c of string) {
    if (c != ' ') {
      if (chars[c.toLowerCase()]) {
        chars[c.toLowerCase()] += 1;
      } else {
        chars[c.toLowerCase()] = 1;
      }
    }
  }
  let count = 0;
  for (const c in chars) {
    count += 1;
  }
  return count;
}



