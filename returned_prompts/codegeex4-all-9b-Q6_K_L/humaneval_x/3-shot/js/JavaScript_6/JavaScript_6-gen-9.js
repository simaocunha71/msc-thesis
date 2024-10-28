  var result = [];
  var current_string = [];
  var current_depth = 0;
  var max_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
      if (current_depth > max_depth) {
        max_depth = current_depth;
      }
    } else if (c == ')') {
      current_depth -= 1;
      current_string.push(c);
      if (current_depth == 0) {
        result.push(max_depth);
        max_depth = 0;
        current_string = [];
      }
    }
  }

  return result;
}