  var result = [];
  var current_string = '';
  var current_depth = 0;
  var max_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      max_depth = Math.max(max_depth, current_depth);
      current_string += c;
    } else if (c == ')') {
      current_depth -= 1;
      current_string += c;
      if (current_depth == 0) {
        result.push(max_depth);
        current_string = '';
        max_depth = 0;
      }
    }
  }

  return result;
}