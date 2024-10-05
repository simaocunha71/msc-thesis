  var max_depth = [];

  for (const group of paren_string.split(' ')) {
    var depth = 0;
    for (const c of group) {
      if (c == '(') {
        depth += 1;
      } else if (c == ')') {
        depth -= 1;
      }
    }
    max_depth.push(depth);
  }

  return max_depth;
}



