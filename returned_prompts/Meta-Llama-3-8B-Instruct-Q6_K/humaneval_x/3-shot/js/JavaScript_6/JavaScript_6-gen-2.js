  var result = [];
  var current_depth = 0;
  var max_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      if (current_depth > max_depth) {
        max_depth = current_depth;
      }
    } else if (c == ')') {
      current_depth -= 1;
    }
  }

  result.push(max_depth);

  var groups = paren_string.split(' ');
  for (const group of groups) {
    current_depth = 0;
    max_depth = 0;
    for (const c of group) {
      if (c == '(') {
        current_depth += 1;
        if (current_depth > max_depth) {
          max_depth = current_depth;
        }
      } else if (c == ')') {
        current_depth -= 1;
      }
    }
    result.push(max_depth);
  }

  return result;
}