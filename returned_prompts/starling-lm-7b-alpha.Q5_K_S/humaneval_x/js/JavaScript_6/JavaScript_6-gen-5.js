  var result = [];
  var max_depth = 0;
  var current_depth = 0;
  var current_group = '';

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      if (current_group.length > 0) {
        current_group += c;
      }
    } else if (c == ')') {
      current_depth -= 1;
      if (current_group.length > 0) {
        current_group += c;
      }
      if (current_depth > max_depth) {
        max_depth = current_depth;
      }
    } else if (c == ' ') {
      result.push(max_depth);
      max_depth = 0;
      current_depth = 0;
      current_group = '';
    }
  }
  if (current_depth > 0) {
    result.push(current_depth);
  }
  return result;
}



