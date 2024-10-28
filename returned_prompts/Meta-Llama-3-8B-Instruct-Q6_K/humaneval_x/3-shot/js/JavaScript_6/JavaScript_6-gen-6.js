  var result = [];
  var current_string = [];
  var current_depth = 0;
  var groups = paren_string.split(' ');

  for (const group of groups) {
    current_string = [];
    current_depth = 0;
    for (const c of group) {
      if (c == '(') {
        current_depth += 1;
        current_string.push(c);
      } else if (c == ')') {
        current_depth -= 1;
        current_string.push(c);
      }
    }
    result.push(current_depth);
  }

  return result;
}