  var result = [];
  var depth = 0;
  var max_depth = 0;
  for (const c of paren_string) {
    if (c == '(') {
      depth += 1;
      max_depth = Math.max(depth, max_depth);
    } else if (c == ')') {
      depth -= 1;
    }
    result.push(max_depth);
  }
  return result;
}



