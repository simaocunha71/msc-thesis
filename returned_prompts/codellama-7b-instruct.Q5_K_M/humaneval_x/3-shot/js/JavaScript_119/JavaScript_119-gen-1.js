  let stack = [];
  for (const c of lst[0]) {
    if (c == '(') {
      stack.push(c);
    } else if (c == ')') {
      stack.pop();
    }
  }
  if (stack.length == 0) {
    stack = [];
    for (const c of lst[1]) {
      if (c == '(') {
        stack.push(c);
      } else if (c == ')') {
        stack.pop();
      }
    }
  }
  if (stack.length == 0) {
    return 'Yes';
  }
  return 'No';
}



