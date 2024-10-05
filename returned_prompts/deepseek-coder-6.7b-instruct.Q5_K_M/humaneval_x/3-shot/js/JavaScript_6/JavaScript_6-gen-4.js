  return paren_string.split(' ').map((group) => {
    var max_depth = 0;
    var current_depth = 0;
    for (const char of group) {
      if (char === '(') {
        current_depth += 1;
        if (current_depth > max_depth) {
          max_depth = current_depth;
        }
      } else if (char === ')') {
        current_depth -= 1;
      }
    }
    return max_depth;
  });
}



