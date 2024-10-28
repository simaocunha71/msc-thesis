  var stack = [];
  for (const b of brackets) {
    if (b == '(') {
      stack.push(b);
    } else if (b == ')') {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}



