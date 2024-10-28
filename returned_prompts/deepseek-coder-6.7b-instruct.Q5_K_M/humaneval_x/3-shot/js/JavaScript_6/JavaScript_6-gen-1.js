  var result = [];
  var groups = paren_string.split(' ');

  for (const group of groups) {
    var max_depth = 0;
    var current_depth = 0;

    for (const c of group) {
      if (c === '(') {
        current_depth++;
        if (current_depth > max_depth) {
          max_depth = current_depth;
        }
      } else if (c === ')') {
        current_depth--;
      }
    }

    result.push(max_depth);
  }

  return result;
}



