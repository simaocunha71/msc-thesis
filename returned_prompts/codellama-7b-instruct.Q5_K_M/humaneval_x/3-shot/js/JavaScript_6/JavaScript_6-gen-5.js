  var result = [];

  for (var group of paren_string.split(' ')) {
    var depth = 0;
    for (var i = 0; i < group.length; i++) {
      if (group[i] == '(') {
        depth += 1;
      } else if (group[i] == ')') {
        depth -= 1;
      }
    }
    result.push(depth);
  }
  return result;
}



