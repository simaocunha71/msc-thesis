  let opening_count = 0;
  for (const c of brackets) {
    if (c == '(') {
      opening_count += 1;
    } else if (c == ')') {
      opening_count -= 1;
      if (opening_count < 0) {
        return false;
      }
    }
  }
  return opening_count == 0;
}



