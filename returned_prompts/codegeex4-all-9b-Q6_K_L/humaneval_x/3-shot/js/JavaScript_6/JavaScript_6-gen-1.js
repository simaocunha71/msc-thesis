  var result = [];
  var current_depth = 0;
  var current_string = [];

  for (const c of paren_string) {
    if (c == '(') {
      current_depth += 1;
      current_string.push(c);
    } else if (c == ')') {
      current_depth -= 1;
      current_string.push(c);
      if (current_depth == 0) {
        result.push(current_string);
        current_string = [];
      }
    }
  }

  return result.map(s => s.length / 2);
}