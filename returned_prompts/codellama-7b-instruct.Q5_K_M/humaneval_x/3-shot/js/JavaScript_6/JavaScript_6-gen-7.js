  var result = [];
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
    } else if (c == ')') {
      current_depth -= 1;
    }

    if (current_depth > 0) {
      if (!result[current_depth]) {
        result[current_depth] = 0;
      }
      result[current_depth] += 1;
    }
  }

  return result;
}



