  var stack = [];
  for (const c of brackets) {
    if (c == '<') {
      stack.push(c);
    } else if (c == '>') {
      if (stack.length > 0 && stack[stack.length-1] == '<') {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return stack.length == 0;
}



