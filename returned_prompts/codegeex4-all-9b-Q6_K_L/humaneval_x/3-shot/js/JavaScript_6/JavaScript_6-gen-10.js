  var result = [];
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
    } else if (c == ')') {
      current_depth -= 1;
    }
    result.push(current_depth);
  }

  return result;
}



