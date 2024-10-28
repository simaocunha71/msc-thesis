  var depths = [];
  var groups = paren_string.split(" ");
  for (var group of groups) {
    var maxDepth = 0;
    var currentDepth = 0;
    for (var char of group) {
      if (char == '(') {
        currentDepth += 1;
        if (currentDepth > maxDepth) {
          maxDepth = currentDepth;
        }
      } else if (char == ')') {
        currentDepth -= 1;
      }
    }
    depths.push(maxDepth);
  }
  return depths;
}



