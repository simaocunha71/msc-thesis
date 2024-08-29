  var result = [];
  var current_depth = 0;
  var current_string = '';

  for (const c of paren_string.split(' ')) {
    if (c == '(') {
      current_depth += 1;
    } else if (c == ')') {
      current_depth -= 1;
    } else {
      result.push(current_depth);
    }
  }

  return result;
}



