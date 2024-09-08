  let stack = [];
  for (const c of brackets) {
    if (c == '<') {
      stack.push(c);
    } else if (c == '>' && stack.length > 0) {
      stack.pop();
    } else {
      return false;
    }
  }
  return stack.length == 0;
}



