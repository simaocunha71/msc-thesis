  var stack = [];
  for (let c of brackets) {
    if (c == '<') {
      stack.push(c);
    } else {
      if (stack.length == 0) {
        return false;
      }
      stack.pop();
    }
  }
  return stack.length == 0;
}



