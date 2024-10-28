  var result = [];
  var current_depth = 0;

  for (const c of paren_string.split(' ')) {
    var depth = 0;
    for (const char of c) {
      if (char == '(') {
        depth += 1;
      } else if (char == ')') {
        depth -= 1;
      }
    }
    result.push(depth);
  }

  return result;
}