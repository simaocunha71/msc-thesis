  var count = 0;
  for (const c of brackets) {
    if (c == "<") {
      count++;
    } else if (c == ">") {
      if (count == 0) {
        return false;
      }
      count--;
    }
  }
  return count == 0;
}