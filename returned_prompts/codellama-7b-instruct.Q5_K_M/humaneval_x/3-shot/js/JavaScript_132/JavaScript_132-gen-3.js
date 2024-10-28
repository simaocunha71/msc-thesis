  var stack = [];
  var open = '[';
  var close = ']';

  for (var i = 0; i < string.length; i++) {
    if (string[i] == open) {
      stack.push(open);
    } else if (string[i] == close) {
      if (stack.length == 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }

  return stack.length == 0;
}



