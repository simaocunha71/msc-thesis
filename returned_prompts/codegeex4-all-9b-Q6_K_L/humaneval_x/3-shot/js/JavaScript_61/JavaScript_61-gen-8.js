  var count = 0;
  for (const c of brackets) {
    if (c == '(') {
      count += 1;
    } else if (c == ')') {
      count -= 1;
      if (count < 0) {
        return false;
      }
    }
  }
  return count == 0;
}



