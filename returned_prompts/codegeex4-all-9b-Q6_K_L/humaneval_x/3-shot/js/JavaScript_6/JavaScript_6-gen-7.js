  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
    } else if (c == ')') {
      current_depth -= 1;
      current_string.push(c);
      if (current_depth == 0) {
        result.push(current_string.join(''));
        current_string = [];
      }
    }
  }

  return result.map(group => {
    var depth = 0;
    var max_depth = 0;
    for (const c of group) {
      if (c == '(') {
        depth += 1;
        if (depth > max_depth) {
          max_depth = depth;
        }
      } else if (c == ')') {
        depth -= 1;
      }
    }
    return max_depth;
  });
}