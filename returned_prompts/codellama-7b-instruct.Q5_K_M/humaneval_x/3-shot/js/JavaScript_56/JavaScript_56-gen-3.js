  var stack = [];
  for (const c of brackets) {
    if (c == '<') {
      stack.push(c);
    } else if (c == '>') {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}



