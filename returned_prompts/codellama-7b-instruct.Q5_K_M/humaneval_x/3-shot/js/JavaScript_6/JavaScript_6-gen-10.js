  var result = [];

  for (let group of paren_string.split(' ')) {
    let depth = 0;
    let current_depth = 0;

    for (const c of group) {
      if (c == '(') {
        current_depth += 1;
      } else if (c == ')') {
        current_depth -= 1;
        if (current_depth < 0) {
          throw new Error('Unmatched parenthesis');
        }
        if (current_depth > depth) {
          depth = current_depth;
        }
      }
    }
    if (current_depth != 0) {
      throw new Error('Unmatched parenthesis');
    }

    result.push(depth);
  }

  return result;
}



