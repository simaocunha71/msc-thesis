  var result = [];
  var depth = 0;
  for (const c of paren_string.split(' ')) {
    if (c[0] == '(') {
      depth += 1;
    } else if (c[0] == ')') {
      depth -= 1;
    }
    result.push(depth);
  }

  return result;
}



