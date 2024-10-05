  let openCount = 0;
  for (const c of brackets) {
    if (c == '<') {
      openCount++;
    } else if (c == '>') {
      openCount--;
      if (openCount < 0) return false;
    }
  }
  return openCount == 0;
}