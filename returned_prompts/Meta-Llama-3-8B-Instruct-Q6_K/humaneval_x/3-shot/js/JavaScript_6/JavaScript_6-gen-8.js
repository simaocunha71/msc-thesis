  var result = [];
  var current_depth = 0;
  var max_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      max_depth = Math.max(max_depth, current_depth);
    } else if (c == ')') {
      current_depth -= 1;
    }
  }

  result.push(max_depth);

  return result;
}