  var stack = [];

  for (const c of lst[0]) {
    if (c == '(') {
      stack.push(c);
    } else {
      if (stack.length == 0) {
        return 'No';
      }
      stack.pop();
    }
  }

  for (const c of lst[1]) {
    if (c == '(') {
      stack.push(c);
    } else {
      if (stack.length == 0) {
        return 'No';
      }
      stack.pop();
    }
  }

  if (stack.length == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}



