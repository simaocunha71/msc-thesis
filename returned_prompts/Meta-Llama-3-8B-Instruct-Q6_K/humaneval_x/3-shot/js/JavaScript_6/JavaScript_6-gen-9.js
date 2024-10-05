  var result = [];
  var current_string = [];
  var current_depth = 0;

  for (const c of paren_string.split(' ')) {
    for (const ch of c) {
      if (ch == '(') {
        current_depth += 1;
        current_string.push(ch);
      } else if (ch == ')') {
        current_depth -= 1;
        current_string.push(ch);
      }
    }
    result.push(current_depth);
    current_string = [];
    current_depth = 0;
  }

  return result;
}