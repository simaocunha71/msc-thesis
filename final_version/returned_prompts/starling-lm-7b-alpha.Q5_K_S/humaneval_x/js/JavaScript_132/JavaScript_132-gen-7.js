  let openCount = 0;

  for (const c of string) {
    if (c == '[') {
      openCount += 1;
    } else if (c == ']') {
      openCount -= 1;
      if (openCount < 0) {
        return true;
      }
    }
  }

  return openCount != 0;
}



