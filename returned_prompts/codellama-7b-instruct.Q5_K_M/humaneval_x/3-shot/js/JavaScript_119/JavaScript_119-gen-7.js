  var stack = [];

  for (const s of lst) {
    if (s == '(') {
      stack.push(s);
    } else {
      if (stack.length == 0) {
        return 'No';
      } else {
        stack.pop();
      }
    }
  }

  if (stack.length == 0) {
    return 'Yes';
  } else {
    return 'No';
  }
}



