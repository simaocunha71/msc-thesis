  var current_depth = 0;

  for (const c of brackets) {
    if (c == '(') {
      current_depth += 1;
    } else if (c == ')') {
      current_depth -= 1;
    }
    if (current_depth < 0) {
      return false;
    }
  }

  return current_depth == 0;
}