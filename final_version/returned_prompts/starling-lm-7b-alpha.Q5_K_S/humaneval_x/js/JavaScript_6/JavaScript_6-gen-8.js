  var result = [];
  var current_depth = 0;

  for (const p of paren_string.split(' ')) {
    var depth = 0;
    for (const c of p) {
      if (c == '(') {
        depth += 1;
      } else if (c == ')') {
        depth -= 1;
      }
      current_depth = Math.max(current_depth, depth);
    }
    result.push(current_depth);
    current_depth = 0;
  }

  return result;
}



