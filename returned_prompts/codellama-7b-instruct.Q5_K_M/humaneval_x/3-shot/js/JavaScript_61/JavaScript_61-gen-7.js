  var stack = [];
  for (var i = 0; i < brackets.length; i++) {
    if (brackets[i] == '(') {
      stack.push(brackets[i]);
    } else {
      if (stack.length == 0) {
        return false;
      } else {
        stack.pop();
      }
    }
  }
  return stack.length == 0;
}



