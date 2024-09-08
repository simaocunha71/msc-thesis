  let max = 0;
  for (const c of string) {
    if (c == '[') {
      max += 1;
    } else {
      max -= 1;
      if (max < 0) {
        return true;
      }
    }
  }
  return max > 0;
}



