  var result = [];
  var current_depth = 0;

  for (const c of paren_string.split(' ')) {
    var depth = 0;
    for (const d of c) {
      if (d == '(') {
        depth += 1;
      } else if (d == ')') {
        depth -= 1;
      }
      current_depth = Math.max(current_depth, depth);
    }
    result.push(current_depth);
  }

  return result;
}



