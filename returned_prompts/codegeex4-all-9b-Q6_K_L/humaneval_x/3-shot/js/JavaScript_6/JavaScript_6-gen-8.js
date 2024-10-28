  var result = [];
  var current_depth = 0;
  var current_group = [];

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_group.push(c);
    } else if (c == ')') {
      current_depth -= 1;
      current_group.push(c);
      if (current_depth == 0) {
        result.push(current_group.length);
        current_group = [];
      }
    }
  }

  return result;
}